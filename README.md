# SassyVoice
Do You Have The Guts 2018 - SAS challenge

# Installation
1. Download Conda (https://conda.io/miniconda.html or https://www.anaconda.com/download)
2. Set up a Conda environment:
    - `conda env create -f environment.yml`
3. Activate the environment:
    - `source activate sassyvoice`
4. Hack

# Updates @ 3:30 AM

I got CMU Sphinx working along with voice regonition API's. I've yet still to try and incorporate that with the CMU Sphinx train in order to better recognise words. The issue was the microphone had picked up ambient noises that messed up the speech recognition. There was a Python method which helped fix that 'r.adjust_for_ambient_noise(source, duration=5)' setting different energy thresholds by listening to Ambient Noise and adjusting the threshold. 

