import streamlit as st

def show_exercise(risk):
    st.subheader("🏋️ PCOS-Focused Exercise Plan")

    if risk == "low":
        st.image("images/exercise_low.jpg", use_column_width=True)
        st.markdown("""
        ### 💃 Light Movement for Hormonal Balance
        - Brisk walking – 30 mins/day  
        - Beginner yoga or Pilates  
        - Weekend swimming or dance  
        - Focus on maintaining routine consistency
        """)
    elif risk == "medium":
        st.image("images/exercise_medium.jpg", use_column_width=True)
        st.markdown("""
        ### 🏃 Moderate-Intensity Workouts
        - Strength training 2–3 times/week  
        - Yoga for pelvic and core muscles  
        - Light jogging or cycling  
        - Stretch daily to reduce insulin resistance
        """)
    elif risk == "high":
        st.image("images/exercise_high.jpg", use_column_width=True)
        st.markdown("""
        ### 🔥 Targeted Anti-PCOS Workouts
        - HIIT 3×/week  
        - Resistance training  
        - Stress-reducing yoga  
        - Prioritize rest and recovery
        """)
