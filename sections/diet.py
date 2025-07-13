import streamlit as st

def show_diet(risk):
    st.subheader("🍽️ Your Personalized Diet Plan")

    if risk == "low":
        st.image("images/diet_low.jpg", use_column_width=True)
        st.markdown("""
        ### 🥗 Balanced Diet for Maintenance
        - Whole grains: brown rice, quinoa, oats  
        - Fresh fruits and vegetables (leafy greens)  
        - Include plant proteins like tofu, legumes  
        - Limit dairy and caffeine  
        - Hydrate well and eat mindfully
        """)
    elif risk == "medium":
        st.image("images/diet_medium.jpg", use_column_width=True)
        st.markdown("""
        ### 🥦 Stabilizing Hormones through Diet
        - Anti-inflammatory foods (berries, turmeric, spinach)  
        - Moderate complex carbs: sweet potatoes, barley  
        - Healthy fats: olive oil, flaxseeds, avocados  
        - Avoid sugar and refined carbs  
        - Herbal teas: spearmint, cinnamon
        """)
    elif risk == "high":
        st.image("images/diet_high.jpg", use_column_width=True)
        st.markdown("""
        ### 🧘 Healing Diet for High PCOS Risk
        - Low glycemic index (GI) foods  
        - High-fiber: broccoli, carrots, beans  
        - Omega-3: walnuts, chia seeds, flax  
        - Avoid dairy, fried foods, red meat  
        - Eat smaller, more frequent meals
        """)
