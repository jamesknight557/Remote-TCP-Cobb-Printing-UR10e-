# Remote Clay Printing with UR10e Robot

This guide explains how to use the robot arm to print with cobb. It involves a few different computer programs working together.

## Overview: The Big Picture

1. **Design to Instructions (Cura)** - We take a 3D model (an .stl file) and turn it into detailed printing instructions (a .gcode file)

2. **Instructions to Robot Language (Python)** - We convert those instructions into a language the robot understands (a .csv file)

3. **Send to Robot (RoboDK)** - We use a simulation program to send the instructions to the real robot arm and make sure everything is safe

4. **Print! (Robot & Pugmill)** - We start the cobb feeder and then tell the robot to begin its printing routine

## Step-by-Step Instructions

### Step 1: Prepare the Printing Instructions with Cura

Cura is a program that creates the path the printer will follow.

1. Open **Ultimaker Cura** on the computer

2. Go to **File > Open...** and select the file named **Cobb Cura Settings.3mf** - This loads all the correct settings for our clay printer

3. Drag your **3D model file** (an .stl file) into the Cura window

4. Click the **"Slice"** button - This generates the toolpath

5. Click **"Save to File"** and save the file as a **.gcode file** - Remember where you save it!
<img width="758" height="492" alt="Screenshot 2025-09-25 110813" src="https://github.com/user-attachments/assets/482cf518-c172-458b-8b83-494cadabc8bc" />
<img width="758" height="492" alt="Screenshot 2025-09-25 110846" src="https://github.com/user-attachments/assets/79c2a410-44a8-4600-a029-6d828acdc6d6" />

### Step 2: Convert for the Robot with Python

We now convert the .gcode file into a simple list (.csv) that the robot can use.

1. Find the **"GCODE to CSV"** tool on the computer (it's a Python file)

2. Open it in your python environment, ensure the gcode file is in the same directory and change the last line of code ot match your GCODE file (**Note** you may have to use pip3 to install some dependencies).

3. The tool will automatically create a new **.csv file** in the same folder, feel free to change the name.
<img width="745" height="991" alt="Screenshot 2025-09-25 111119" src="https://github.com/user-attachments/assets/69ed19da-f8e3-4db0-916d-7d6f9edba9c7" />

### Step 3: Set Up the Robot in RoboDK

RoboDK is the program that controls the robot arm. We use it to check everything is safe before printing.

#### Connect to the Robot:

1. Open the **RoboDK simulation file** for this project

2. Click the **"Connect"** button in the top menu

3. Enter the robot's **IP Address** (This can be found on the teach pendant)

4. Click **"Connect"**

5. **Important:** Ensure the physical robot is in **REMOTE mode**
<img width="1918" height="1136" alt="Screenshot 2025-09-25 111324" src="https://github.com/user-attachments/assets/a8a1ecf2-65ce-4e8e-966c-9c019b97ed01" />

#### Load the Toolpath:


1. Drag the **.csv file** you created in Step 2 into the RoboDK window

2. A new item will appear - **Right-click** it and select **"Attach to Tool"**

#### Position the Path:

1. Move the path so it sits correctly on the virtual print bed - The first layer must be **flush with the bed surface**

#### Adjust Settings (if needed):

1. **Right-click** the toolpath and select **"Edit Curve"**

2. Here you can change the **printing speed**, the **bed angle**, and how the robot **approaches/retracts the bed**
<img width="1088" height="1107" alt="Screenshot 2025-09-25 111417" src="https://github.com/user-attachments/assets/1a57fad0-42f3-4b85-b593-9be458db94b1" />

### Step 4: Start the Print

Now we get the clay flowing and start the robot.

#### Start the Clay System:

1. Turn on the **Pugmill** (the clay feeder)

2. Turn on the **Auger** (the screw that pushes clay out of the nozzle)

#### Start the Robot Program:

1. In RoboDK, **double-click** the program you created to run it

2. Before running ensure **run on robot** is checked or else you will just see the simualtion

3. At any point press the emergcncy stop on the pendant to stop the robot
<img width="1917" height="1107" alt="Screenshot 2025-09-25 111456" src="https://github.com/user-attachments/assets/52fad376-86ae-4512-8ad0-fc61be683d49" />

## File Reference

- **.stl** - 3D Model File (Step 1: Cura)
- **.3mf** - Cura Settings Profile (Step 1: Cura)
- **.gcode** - Printer Instructions (Step 1 & 2: Cura → Python)
- **.csv** - Robot Path File (Step 3: RoboDK)

## Safety Checklist

- [ ] Robot is in **REMOTE mode** before connecting
- [ ] Path is properly positioned in RoboDK simulation
- [ ] **"Run on Robot"** is enabled before starting
- [ ] Area around robot is clear of people and obstacles
- [ ] Emergency stop button is accessible

## Video Tutorial

A video showing this entire process is available here: [Insert Link to Your Video Here]

## Troubleshooting

**Robot won't connect?**
- Check that the robot is powered on and in **REMOTE mode**
- Verify the **IP address** is correct
- Ensure the computer is on the same network as the robot

**Clay not extruding properly?**
- Check that the **pugmill** and **auger** are running
- Verify clay consistency is appropriate
- Check for nozzle clogs

## Need Help?

If you encounter problems or have questions, please contact: jamesknight557@gmail.com
