NeuroRest

Exploring EEG Alpha Activity During Eyes-Open and Eyes-Closed Resting States

NeuroRest is a small neuroscience project I started to learn how EEG signals can be analysed using Python. I wanted to explore alpha-band activity and see how it differs between eyes-open and eyes-closed resting-state recordings.

I'm an MBBS student interested in neuroscience and research, and this project is part of my effort to learn research methods by working with real data rather than just reading about them.

What I did

- Worked with resting-state EEG recordings.
- Loaded and explored the data using MNE-Python in Google Colab.
- Looked at EEG channels, recording duration and sampling frequency.
- Used Welch's method to estimate power spectral density.
- Calculated preliminary relative alpha power in the 8–13 Hz band.
- Created a graph comparing the eyes-open and eyes-closed recordings.

Dataset

I used data from OpenNeuro:

"OpenNeuro dataset ds007987" (https://openneuro.org/datasets/ds007987/versions/1.1.0)

For this initial analysis, I worked with participant 05, run 1, for both eyes-open and eyes-closed conditions.

Tools used

- Python
- Google Colab
- MNE-Python
- NumPy
- SciPy
- Matplotlib

Initial observation

My first calculation showed higher relative alpha power in the eyes-closed recording than in the eyes-open recording.

These are only preliminary values from one participant. I have not yet completed all the checks needed to confirm the accuracy of the channel selection, signal quality and analysis. So, I am treating this as an initial observation rather than a scientific conclusion.

What I learned

This project helped me get started with EEG data, Python-based signal analysis and scientific visualisation. I also learned that getting a graph is only one part of the process; checking the quality of the data and understanding the limitations are equally important.

Current status

This is a beginner learning project and is still exploratory. Further validation and analysis across more participants would be needed before drawing stronger conclusions.

About me

I'm an MBBS student interested in neuroscience, medical research and learning new ways to work with clinical and biological data.

Thanks for checking out NeuroRest!
