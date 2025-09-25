**Remote Clay Printing with UR10e Robot**
This guide explains how to use the robot arm to print with clay. It involves a few different computer programs working together.

**Overview: The Big Picture**
Think of this process like sending a digital recipe to a robotic chef:

Design to Instructions (Cura) - We take a 3D model (an .stl file) and turn it into detailed printing instructions (a .gcode file)

Instructions to Robot Language (Python) - We convert those instructions into a language the robot understands (a .csv file)

Send to Robot (RoboDK) - We use a simulation program to send the instructions to the real robot arm and make sure everything is safe

Print! (Robot & Pugmill) - We start the clay feeder and then tell the robot to begin its printing routine

**Step-by-Step Instructions**
**Step 1:** Prepare the Printing Instructions with Cura
Cura is a program that creates the path the printer will follow.

Open Ultimaker Cura on the computer

Go to File > Open... and select the file named Cobb Cura Settings.3mf - This loads all the correct settings for our clay printer

Drag your 3D model file (an .stl file) into the Cura window

Click the "Slice" button - This generates the toolpath

Click "Save to File" and save the file as a .gcode file - Remember where you save it!

Step 2: Convert for the Robot with Python
We now convert the .gcode file into a simple list (.csv) that the robot can use.

Find the "GCODE to CSV" tool on the computer (it's a Python file)

Double-click to run it - A black window might pop up

It will ask you for the .gcode file you just made - Find and select that file

The tool will automatically create a new .csv file in the same folder

Step 3: Set Up the Robot in RoboDK
RoboDK is the program that controls the robot arm. We use it to check everything is safe before printing.

Connect to the Robot:

Open the RoboDK simulation file for this project

Click the "Connect" button in the top menu

Enter the robot's IP Address (you will be given this number)

Click "Connect"

Important: Ensure the physical robot is in REMOTE mode

Load the Toolpath:

Drag the .csv file you created in Step 2 into the RoboDK window

A new item will appear - Right-click it and select "Attach to Tool"

Position the Path:

Move the path so it sits correctly on the virtual print bed - The first layer must be flush with the bed surface

Adjust Settings (if needed):

Right-click the toolpath and select "Edit Curve"

Here you can change the printing speed, the bed angle, and how the robot approaches the bed

Step 4: Start the Print
Now we get the clay flowing and start the robot.

Start the Clay System:

Turn on the Pugmill (the clay feeder)

Turn on the Auger (the screw that pushes clay out of the nozzle)

Start the Robot Program:

In RoboDK, double-click the program you created to run it

A window will appear - Make sure "Run on Robot" is ENABLED (checked)

Press "Start" to begin the printing process

File Reference
.stl - 3D Model File (Step 1: Cura)

.3mf - Cura Settings Profile (Step 1: Cura)

.gcode - Printer Instructions (Step 1 & 2: Cura → Python)

.csv - Robot Path File (Step 3: RoboDK)

Safety Checklist
Robot is in REMOTE mode before connecting

Path is properly positioned in RoboDK simulation

"Run on Robot" is enabled before starting

Area around robot is clear of people and obstacles

Emergency stop button is accessible

Video Tutorial
A video showing this entire process is available here: [Insert Link to Your Video Here]

Troubleshooting
Robot won't connect?

Check that the robot is powered on and in REMOTE mode

Verify the IP address is correct

Ensure the computer is on the same network as the robot

Clay not extruding properly?

Check that the pugmill and auger are running

Verify clay consistency is appropriate

Check for nozzle clogs

Need Help?
If you encounter problems or have questions, please contact: [Your Name/Team Here]
