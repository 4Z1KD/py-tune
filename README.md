# pytune 🌺
tuning script for tuner-less transmitters 📻

# prerequisite 🖐️
1. OmniRig (http://dxatlas.com/omnirig/)
3. python (https://www.python.org/downloads/)

# Installation 🛠
1. create virtual environment (https://docs.python.org/3/library/venv.html) ☁️
2. activate the venv (Scripts\activate.bat) 🌬️
3. copy this project's files to the venv directory 📑
4. install the requirements (pip install -r requirements.txt) 🧰

# usage 🚀
launch pytune.bat (this will activate the venv and run the script)

# how it works? 🐜
the script uses omnirig to send a ptt command to Rig1.<br/>
it then plays a 800hz tone through the 2nd output sound device in the device list (assuming this device is the one connected to the radio).<br/>
after a 5 seconds delay, it releases the ptt and stops playing the tone.<br/>

73,<br/>
Gil 4Z1KD
