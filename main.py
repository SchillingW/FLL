#!/usr/bin/env python3
from Launches import Launches
from Robot import MakeRobot, RunLaunch

# Define the robot.
WheelDistance = 11.5 #cm
WheelDiameter = 4.0 #cm

TankBase = ["B", "C"]
MedMotors = ["A", "D"]
Ultrasonic = "1"
Color1 = "2"
Color2 = "3"
Gyro = "4"

Robot = MakeRobot(WheelDistance, WheelDiameter, TankBase, MedMotors, Ultrasonic, Color1, Color2, Gyro)

# Declare variables.
SelectedLaunch = 0
MaxLaunch = len(Launches) - 1

# Main loop.
while True:

    # Display the number of the selected launch.
    Robot.Display(SelectedLaunch + 1)

    # Wait for a button to be pressed. Record which button was pressed.
    LeftPressed = Robot.Button("LEFT")
    RightPressed = Robot.Button("RIGHT")
    UpPressed = Robot.Button("UP")
    while (not LeftPressed) and (not RightPressed) and (not UpPressed):
        LeftPressed = Robot.Button("LEFT")
        RightPressed = Robot.Button("RIGHT")
        UpPressed = Robot.Button("UP")
    
    # Run the selected launch if up was pressed.
    if UpPressed:
        LaunchExited = RunLaunch(Launches[SelectedLaunch], Robot)
        # Increase SelectedLaunch if the launch was not exited by the user.
        if not LaunchExited:
            SelectedLaunch += 1
    
    # Change SelectedLaunch based on user input.
    elif RightPressed:
        SelectedLaunch += 1
    elif LeftPressed:
        SelectedLaunch -= 1
    
    # Loop SelectedLaunch if too big or small.
    if SelectedLaunch < 0:
        SelectedLaunch = MaxLaunch
    if SelectedLaunch > MaxLaunch:
        SelectedLaunch = 0
    
    # Wait for all buttons to be released.
    while Robot.Button("LEFT") or Robot.Button("RIGHT") or Robot.Button("UP"):
        pass
