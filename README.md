bno055_test.py outputs Euler, linear acceleration, and temperature from the sensor.

The openGL_test.py displays a cube which follows the euler rotation of the sensor.

requirements.txt is used to install all the required librarys in the venv.

Below is a guide on how to connect to the raspberry pi and run these files:

Steps to connect to pi with SSH and VNC Viewer:

1) Connect ethernet and power to pi
2) Ssh into the pi via command prompt (in my case: ssh exoskeleton1@raspberrypi)
- Pi will ask for password, in this case MacExo
- If it does not ask for a password… Keep running the ssh command? Idk whats the actual fix but that worked for me lol
To connect to VNC Viewer, must get ip address of the pi (my pi had ip address 192.168.137.152, not sure if this changes)
3) Run hostname -I, should display pi’s ip address
- If it does not, follow these steps (apparently this is an issue with connecting the ethernet cable to the laptop, thank you chatgpt <3 )
  Open Network Connections:
  Press Win + R, type ncpa.cpl, and press Enter.
  Enable Internet Sharing:
  Right-click on your Wi-Fi connection (the one connected to your network) and choose Properties.
  Go to the Sharing tab.
  Check the box that says Allow other network users to connect through this computer’s Internet connection.
  Under "Home networking connection," select the Ethernet connection that’s connected to your Raspberry Pi (e.g., Ethernet or Local Area Connection).
  Apply the Settings and close the window.
  
4) Open VNC Viewer, use the ip address of the pi, and same credentials as above to log into the pi

Next steps are for python setup (idk how to run the c++ code):
Next step is to create the virtual environment (venv) for the pi. This is apparently best practice and also it didn’t let me pip install everything onto the pi directly so we are using a venv 🙂

5) If the pi is already set up with the venv, simply open the pi terminal and run this command and continue to next step:  source bno055_env/bin/activate
If it is not set up, download the files from my github (specifically requirements.txt) and run these commands:
python -m venv bno055_env
source bno055_env/bin/activate
Pip install -r requirements.txt

This will install all the required libraries to the virtual environment. 

6) You are basically done! You can download the files from the github or create you own and run them in the venv via this command in the terminal (replace <filename> with the actual filename):
python3 <filename>.py 
