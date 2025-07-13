import matplotlib.pyplot as plt
import streamlit as st

def display_risk_bar(risk_level):
    levels = ['Low', 'Medium', 'High']
    colors = ['#A8DADC', '#F4A261', '#E76F51']
    values = [1 if levels[i] == risk_level else 0 for i in range(3)]

    fig, ax = plt.subplots()
    bars = ax.bar(levels, values, color=colors)
    ax.set_ylim(0, 1)
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height, f"{int(height*100)}%", ha='center')
    st.pyplot(fig)
```

Let me know if you want me to give `app.py` content here as well!
