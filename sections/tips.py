import streamlit as st

def show_tips(risk):
    st.subheader("💡 Lifestyle & Self-Care Tips")

    if risk == "low":
        st.image("images/tips_low.jpg", use_column_width=True)
        st.markdown("- Consistent sleep & meals\n- Hydrate\n- Track mood")
    elif risk == "medium":
        st.image("images/tips_medium.jpg", use_column_width=True)
        st.markdown("- Avoid skipping meals\n- Use period apps\n- Journal, meditate")
    elif risk == "high":
        st.image("images/tips_high.jpg", use_column_width=True)
        st.markdown("- Rest & recover\n- Cut caffeine after 4 PM\n- See doctor weekly")
