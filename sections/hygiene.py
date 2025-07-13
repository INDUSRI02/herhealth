import streamlit as st

def show_hygiene(risk):
    st.subheader("🧼 PCOS Hygiene Recommendations")

    if risk == "low":
        st.image("images/hygiene_low.jpg", use_column_width=True)
        st.markdown("""
        ### 💧 Daily Hygiene Checklist
        - Bathe gently daily  
        - Use pH-balanced intimate wash  
        - Wear cotton underwear  
        - Track cycle
        """)
    elif risk == "medium":
        st.image("images/hygiene_medium.jpg", use_column_width=True)
        st.markdown("""
        ### 🧼 Balanced Hygiene Routine
        - Avoid scented soaps  
        - Change pads every 4–6 hrs  
        - Treat acne with salicylic acid  
        - Wash oily scalp regularly
        """)
    elif risk == "high":
        st.image("images/hygiene_high.jpg", use_column_width=True)
        st.markdown("""
        ### 💪 Intense Care for Skin & Scalp
        - Exfoliate gently 2×/week  
        - Use sulfate-free shampoos  
        - Seek dermatological help  
        - Prevent sweat rashes
        """)
