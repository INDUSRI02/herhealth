import streamlit as st

def show_motivation(risk):
    st.subheader("💖 Motivation & Mental Health")

    if risk == "low":
        st.image("images/motivation_low.jpg", use_column_width=True)
        st.markdown("> "You are glowing! Keep your routine.")
    elif risk == "medium":
        st.image("images/motivation_medium.jpg", use_column_width=True)
        st.markdown("> "Healing takes time. You’re doing great.")
    elif risk == "high":
        st.image("images/motivation_high.jpg", use_column_width=True)
        st.markdown("> "You are a warrior, even on hard days."")
