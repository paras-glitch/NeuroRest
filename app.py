
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="NeuroRest | EEG Project",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 NeuroRest")
st.subheader(
    "Exploring EEG Alpha Activity During Rest"
)

st.markdown(
    "**A beginner computational neuroscience project** "
    "by Paras Choudhary, MBBS student."
)

st.markdown("---")

# Project overview
st.header("1. About the Project")

st.write("""
NeuroRest is a small exploratory project designed to
introduce electroencephalography (EEG) analysis using
Python. It examines resting-state recordings obtained
under two conditions: eyes open and eyes closed.

EEG records electrical potential differences measured
at the scalp. These signals contain rhythmic activity
that can be studied using signal-processing methods.
One rhythm of interest is alpha activity, conventionally
studied within the 8–13 Hz frequency range.
""")

# Research question
st.header("2. Research Question")

st.write("""
How does the estimated relative alpha-band power differ
between eyes-open and eyes-closed resting recordings
from the same participant?
""")

st.info(
    "Scientific context: alpha activity is often prominent "
    "during relaxed wakefulness with eyes closed, especially "
    "over posterior scalp regions. Opening the eyes often "
    "reduces this activity, a phenomenon called alpha reactivity."
)

# Objectives
st.header("3. Objectives")

st.markdown("""
- Explore publicly available resting-state EEG data.
- Learn how to load EEG recordings with MNE-Python.
- Estimate signal power across frequency bands.
- Compare preliminary alpha-band power estimates.
- Build a reproducible starting point for learning EEG analysis.
""")

# Methodology
st.header("4. Methodology")

st.markdown("""
**Dataset:** [OpenNeuro dataset ds007987](https://openneuro.org/datasets/ds007987/versions/1.1.0)

**Conditions:** Eyes open and eyes closed.

**Participant:** One participant in the initial exploration.

**Tools used:**
- Python
- MNE-Python for EEG data handling
- SciPy for spectral analysis
- NumPy for numerical operations
- Matplotlib for plotting
- Google Colab for execution
""")

st.subheader("Analysis approach")

st.write("""
Power spectral density (PSD) can be estimated using
Welch's method, which averages spectral estimates
from overlapping segments of a signal.

Relative alpha power is calculated as:
""")

st.latex(
    r"\\text{Relative alpha power (\\%)} = "
    r"\\frac{\\text{Power from 8–13 Hz}}"
    r"{\\text{Power from 1–40 Hz}} \\times 100"
)

st.caption(
    "This formula describes the initial analysis approach. "
    "The channel selection, signal scaling, preprocessing "
    "and implementation still require validation."
)

# Results
st.header("5. Preliminary Results")

st.warning(
    "Exploratory values only: these estimates have not been "
    "validated for channel selection, artifacts or signal quality."
)

open_power = 9.87
closed_power = 20.39

col1, col2 = st.columns(2)
col1.metric("Eyes-open estimate", f"{open_power:.2f}%")
col2.metric("Eyes-closed estimate", f"{closed_power:.2f}%")

fig, ax = plt.subplots(figsize=(7, 4))
bars = ax.bar(
    ["Eyes open", "Eyes closed"],
    [open_power, closed_power]
)
ax.set_ylabel("Relative alpha power (%)")
ax.set_title("Initial comparison of resting EEG conditions")
ax.set_ylim(0, 25)
ax.bar_label(bars, fmt="%.2f%%")
fig.tight_layout()

st.pyplot(fig)
plt.close(fig)

st.write("""
The initial calculation produced a higher relative
alpha-power estimate in the eyes-closed recording.
This is consistent with the general physiological pattern
often described in resting EEG, but this single exploratory
analysis cannot establish a reliable finding.
""")

# Limitations
st.header("6. Limitations")

st.markdown("""
- Only one participant was explored.
- EEG channels and auxiliary sensors need careful identification.
- Signal quality and artifacts have not been fully assessed.
- Electrode locations and regional differences have not been validated.
- The current estimates should not be generalized to other people.
- This project is educational and is not a diagnostic tool.
""")

# Future work
st.header("7. Future Directions")

st.markdown("""
Possible next steps, after validating the analysis, include:

- Selecting verified scalp EEG channels.
- Applying appropriate artifact handling and preprocessing.
- Repeating the analysis across multiple participants.
- Comparing alpha activity across scalp regions.
- Improving the reproducibility and documentation of the workflow.
""")

# Links
st.header("8. Project Resources")

st.markdown("""
- [OpenNeuro dataset](https://openneuro.org/datasets/ds007987/versions/1.1.0)
- [Source notebook on GitHub](https://github.com/paras-glitch/NeuroRest)
- [MNE-Python spectral analysis guide](https://mne.tools/stable/auto_tutorials/time-freq/10_spectrum_class.html)
""")

st.markdown("---")
st.caption(
    "NeuroRest | An independent learning project in "
    "computational neuroscience. Preliminary analysis; "
    "not peer-reviewed or clinically validated."
)
