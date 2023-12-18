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


**Documentation for the diffrent buttons and options:**

*Start Timer Button* - As labeled, starts the countdown timer when the match starts

*Stop Timer Button* - Stops and resets the timer

*Hide/Show Timer Button* - On the display screen, you will need to supply your own google sheets/excel/sheets platform to display scores. You will need to place the timer widow over this window, and when the button is pressed the timer window will hide so the spreadsheet is displayed.

*Volume Up/Down Buttons* - These will fade the volume to the specified higher/lower volume.

*Volume Sliders* - The first slider is where you can specify the volume you want to fade down to when the volume down button is pressed. The one on the right will specify the volume to fade to when the volume up button is pressed.

*Drop-Down (Windows Only)* - This menu is the place you can select the application to change the volume for. Only this app's master volume will be changed.

*Change Timer Background Button* - this will open a color selector menu to select a new color for the background of the timer window.

*Toggle Full Screen Button* - This will toggle full screen for the timer (display) window.
