import streamlit as st
import pickle
from backend.auth import *
from sections import diet, exercise, hygiene, motivation, tips
from utils.risk_graph import display_risk_bar
import os

# Load the trained model
model = pickle.load(open("model/pcos_model.pkl", "rb"))

# Initialize DB tables
create_user_table()
create_prediction_table()

# Sidebar Navigation
st.sidebar.title("HerHealth+ Navigation")
page = st.sidebar.selectbox("Select Page", ["Login", "Register", "Predict Risk", "Recommendations"])

# Session
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.session_state.risk = ""

# Login Page
if page == "Login":
    st.title("🔐 Welcome to HerHealth+ Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    if st.button("Login"):
        hashed = hash_password(password)
        result = login_user(username, hashed)
        if result:
            st.success(f"Welcome back, warrior ✨ {username}!")
            st.session_state.logged_in = True
            st.session_state.username = username
        else:
            st.error("Invalid username or password")

# Register Page
elif page == "Register":
    st.title("📝 Register to HerHealth+")
    new_user = st.text_input("New Username")
    new_password = st.text_input("New Password", type='password')
    if st.button("Register"):
        add_user(new_user, hash_password(new_password))
        st.success("Registration successful! Please login.")

# Prediction Page
elif page == "Predict Risk":
    if not st.session_state.logged_in:
        st.warning("Please login first.")
    else:
        st.title("📊 PCOS Risk Prediction")
        st.markdown("Fill out the details below:")

        age = st.slider("Age", 12, 50, 25)
        weight = st.number_input("Weight (kg)", min_value=30.0, max_value=150.0)
        height = st.number_input("Height (cm)", min_value=120.0, max_value=200.0)
        cycle_length = st.slider("Cycle Length (days)", 15, 40, 28)

        irregular_periods = st.selectbox("Irregular Periods?", ["No", "Yes"])
        facial_hair = st.selectbox("Excess Facial Hair?", ["No", "Yes"])
        acne = st.selectbox("Acne?", ["No", "Yes"])
        hair_loss = st.selectbox("Hair Loss?", ["No", "Yes"])
        dark_patches = st.selectbox("Dark Skin Patches?", ["No", "Yes"])

        # Convert inputs
        data = [[
            age, weight, height, cycle_length,
            1 if irregular_periods == "Yes" else 0,
            1 if facial_hair == "Yes" else 0,
            1 if acne == "Yes" else 0,
            1 if hair_loss == "Yes" else 0,
            1 if dark_patches == "Yes" else 0
        ]]

        if st.button("Predict My Risk"):
            prediction = model.predict(data)[0]
            if prediction == 2:
                risk = "High"
            elif prediction == 1:
                risk = "Medium"
            else:
                risk = "Low"

            st.session_state.risk = risk
            st.success(f"💥 Your predicted PCOS risk is: **{risk}**")
            display_risk_bar(risk)

            log_prediction(
                st.session_state.username, age, weight, height, cycle_length,
                data[0][4], data[0][5], data[0][6], data[0][7], data[0][8], risk
            )

# Recommendation Page
elif page == "Recommendations":
    if not st.session_state.logged_in or not st.session_state.risk:
        st.warning("Please predict your risk first.")
    else:
        st.title("💖 Personalized Recommendations")
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["Diet", "Exercise", "Hygiene", "Motivation", "Tips"])

        with tab1:
            diet.show_diet(st.session_state.risk.lower())
        with tab2:
            exercise.show_exercise(st.session_state.risk.lower())
        with tab3:
            hygiene.show_hygiene(st.session_state.risk.lower())
        with tab4:
            motivation.show_motivation(st.session_state.risk.lower())
        with tab5:
            tips.show_tips(st.session_state.risk.lower())
