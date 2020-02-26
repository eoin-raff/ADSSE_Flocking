# ADSSE_Flocking
Flocking Simulator example for MED8 Algorithms, Data Structures and Software Engineering course

## Installing GLFW
This demo uses p5py, which is a python port of the javascript library p5js (which is in turn based on processing).
In order to use p5py, we first need to install the Graphics Library Framework (GLFW).

### Mac
For mac users it is easy to install this 
* `brew install glfw`

### Linux (Ubuntu / Debian)
Likewise, it is easy to install GLFW on most linux systems:
* `sudo apt-get install libglfw3`

### Windows
Unfortunately it is not so easy to install GLFW on windows. Try the following steps:
1. Download the latest version of GLFW from this link: https://www.glfw.org/download.html

... Note: I recommend getting the 32-bit binaries, even though you are likely on a 64-bit system (this is simply the only way it worked for me)
2. Extract the to an easy to find location (e.g. `C:\GLFW\`). It is most important to ensure to this folder now contains `\include\` and `\lib-mingw\`
3. Open the command prompt *as an administrator*
  ..1. Open the start menu and type "cmd"
  ..2. Right-click on "Command Prompt"
  ..3. Select "Run as administrator"
4. Enter the command `python -m pip install -U --force glfw-cffi`

GLFW is now installed, but you still have to add it to the system environment, so that it can be used.
1. Locate the Environment Variables window
  ..1. Open the Control Panel and navigate to the System panel
  ..2. On the left, click on "Advanced System Settings"
  ..3. In the pop-up window, selecet "Environment Variables"
2. Create a new user variable
3. Name it `GLFW_LIBRARY` and set the value to `C:\GLFW\lib-mingw\glfw3.dll`, or whatever the equivilant directory address for that file is on your device.
4. Select OK on all the open menus, then you are ready to install p5

## Install p5
* Open CMD or a python terminal and run the command `pip install p5`

... Note: if this gives you permission errors, try either `pip install p5 --user` or `python -m pip install p5`
