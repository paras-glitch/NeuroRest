
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="NeuroRest",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 NeuroRest")
st.subheader("EEG Alpha Power Analysis")
st.write(
    "An exploratory MBBS student project comparing "
    "eyes-open and eyes-closed resting EEG."
)

open_power = 9.87
closed_power = 20.39

col1, col2 = st.columns(2)

col1.metric("Eyes Open", f"{open_power}%")
col2.metric("Eyes Closed", f"{closed_power}%")

st.subheader("Relative Alpha Power Comparison")

fig, ax = plt.subplots()
ax.bar(
    ["Eyes Open", "Eyes Closed"],
    [open_power, closed_power]
)
ax.set_ylabel("Relative Alpha Power (%)")
ax.set_ylim(0, 25)

st.pyplot(fig)

st.info(
    "These are preliminary estimates from an initial "
    "analysis of one participant. Channel selection, "
    "signal quality and preprocessing require validation. "
    "They are not confirmed scientific findings."
)

st.caption(
    "Tools: Python, MNE-Python, SciPy, Matplotlib and Colab"
)

st.markdown(
    "[Source notebook on GitHub]"
    "(https://github.com/paras-glitch/NeuroRest)"
)
