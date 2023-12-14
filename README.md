📖 Instructions
Make sure you have Python 3 installed and working.

Clone the repo:

`git clone https://github.com/DueWesternersProgramming/FLL-Music-Project.git`

If you are running Linux, you will need to install the library *libasound2-dev*
e.g. `sudo apt install libasound2-dev -y`.
This package uses the ALSA system for audio volume control on Linux.

Install prerequisites using pip, preferably in a new environment:
`pip install -r requirements.txt`

Run the *Main.py* file to start the application. The controller tab will house
all if your controllers to start the timer and fade the volume. Full screen
for the controller is not required due to scaling, but scale up the display/timer screen
to the size of your screen.

If you want to build a fully-packaged executable file, run the *Build.py* file.
Linux users, if you plan to build the project for distribution, you will need two more packages.
Look at this [link](https://pyinstaller.org/en/stable/requirements.html#gnu-linux) for more information.

If any issues arise, please open an issue [here](https://github.com/DueWesternersProgramming/FLL-Music-Project/issues).
