#!/usr/bin/env python3
class MakeRobot:

    def __init__(Self, WheelDistance, WheelDiameter, TankBase, MedMotors, Ultrasonic, Color1, Color2, Gyro): # WheelDistance and WheelDiameter in cm.
        # Import the parts of the robot.
        from ev3dev2.button import Button
        from ev3dev2.display import Display
        from ev3dev2.motor import MoveTank, MediumMotor, LargeMotor, SpeedRPS, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
        from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
        from ev3dev2.sensor.lego import UltrasonicSensor, ColorSensor, GyroSensor
        # Define the ports.
        Ports = {"A" : OUTPUT_A, "B" : OUTPUT_B, "C" : OUTPUT_C, "D" : OUTPUT_D,
                 "1" :  INPUT_1, "2" :  INPUT_2, "3" :  INPUT_3, "4" :  INPUT_4}
        # Define the parts of the robot.
        Self.SpeedRPS = SpeedRPS
        Self.WheelDistance = WheelDistance
        Self.WheelCircumference = WheelDiameter * 3.1415
        Self.TankBase = MoveTank(Ports[TankBase[0]], Ports[TankBase[1]])
        Self.DriveMotor = LargeMotor(Ports[TankBase[0]]) # Used only for sensing degrees.
        Self.MedMotors = [MediumMotor(Ports[MedMotors[0]]), MediumMotor(Ports[MedMotors[1]])]
        Self.Ultrasonic = UltrasonicSensor(Ports[Ultrasonic])
        Self.Color1 = ColorSensor(Ports[Color1])
        Self.Color2 = ColorSensor(Ports[Color2])
        Self.Gyro = GyroSensor(Ports[Gyro])
        Self.Buttons = Button()
        Self.LCD = Display()

    # In launch functions.

    def SpeedCPS(Self, Speed): # Speed in cm/sec.
        # Convert Speed from cm/sec into RPS, then into an amount compatible with the motors using the SpeedRPS function.
        return Self.SpeedRPS(Speed / Self.WheelCircumference)

    def Drive(Self, Args): # Speed in cm/sec. Distance in cm.
        (Speed, Distance) = Args
        # Get motor angle information.
        Start = Self.DriveMotor.position
        DegreesMoved = Distance / Self.WheelCircumference * 360
        End = Start + DegreesMoved
        # Turn on the motors.
        Self.TankBase.on(Self.SpeedCPS(Speed), Self.SpeedCPS(Speed))
        # Wait for the motor to be at the correct angle.
        LaunchExited = False
        while ((End > Self.DriveMotor.position and Speed > 0) # Use this condition when the motor position is increasing (Speed > 0).
                or
               (End < Self.DriveMotor.position and Speed < 0)):  # Use this condition when the motor position is decreasing (Speed < 0).
            if Self.Button("DOWN"):
                LaunchExited = True
                break
        # Turn off the motors.
        Self.TankBase.off()
        # Return a boolean for whether or not the the launch was ended by the user.
        return LaunchExited
        
    def DriveUltrasonic(Self, Args): # Speed in cm/sec. TargetDistance in cm.
        (Speed, TargetDistance) = Args
        # Turn on the motors.
        Self.TankBase.on(Self.SpeedCPS(Speed), Self.SpeedCPS(Speed))
        # Wait for the ultrasonic to be at TargetDistance.
        LaunchExited = False
        while ((TargetDistance > Self.Ultrasonic.distance_centimeters and Speed > 0) # Use this condition when the distance is increasing (Speed > 0).
                or
               (TargetDistance < Self.Ultrasonic.distance_centimeters and Speed < 0)):  # Use this condition when the distance is decreasing (Speed < 0).
            if Self.Button("DOWN"):
                LaunchExited = True
                break
        # Turn off the motors.
        Self.TankBase.off()
        # Return a boolean for whether or not the the launch was ended by the user.
        return LaunchExited
        
    def Turn(Self, Args): # Radius in cm. DegPerSec in deg/sec. TargetDegree in deg.
        (Radius, DegPerSec, TargetDegree) = Args
        # Calculate the radius of each wheel's path.
        LeftRadius = Radius + Self.WheelDistance / 2
        RightRadius = Radius - Self.WheelDistance / 2
        # Calculate the circumference of each wheel's path.
        LeftCircumference = LeftRadius * 2 * 3.1415
        RightCircumference = RightRadius * 2 * 3.1415
        # Caluclate the distance per degree of each wheel's path.
        LeftCmPerDeg = LeftCircumference / 360
        RightCmPerDeg = RightCircumference / 360
        # Calculate each wheel's speed.
        LeftSpeed = LeftCmPerDeg * DegPerSec
        RightSpeed = RightCmPerDeg * DegPerSec
        # Turn the drive motors on.
        Self.TankBase.on(Self.SpeedCPS(LeftSpeed), Self.SpeedCPS(RightSpeed))
        # Wait for gyro to be at TargetDegree.
        LaunchExited = False
        while ((TargetDegree > Self.Gyro.angle and DegPerSec > 0) # Use this condition when the degree is increasing (DegPerSec > 0).
                or
               (TargetDegree < Self.Gyro.angle and DegPerSec < 0)): # Use this condition when the degree is decreasing (DegPerSec < 0).
            if Self.Button("DOWN"):
                LaunchExited = True
                break
        # Turn off the motors.
        Self.TankBase.off()
        # Return a boolean for whether or not the the launch was ended by the user.
        return LaunchExited
        
    def MotorOn(Self, Args): # MotorNum is 0 or 1 for which motor is affected. Speed in cm/sec.
        (MotorNum, Speed) = Args
        Self.MedMotors[MotorNum].on(Self.SpeedRPS(Speed))

    def MotorOff(Self, Args): # MotorNum is 0 or 1 for which motor is affected.
        MotorNum = Args[0]
        Self.MedMotors[MotorNum].off()
        
    def Wait(Self, Args): # Seconds in sec.
        Seconds = Args[0]
        from time import time as Time
        # Get timing information.
        End = Time() + Seconds
        # Wait for the time to be up.
        LaunchExited = False
        while End > Time():
            if Self.Button("DOWN"):
                LaunchExited = True
                break
        # Return a boolean for whether or not the the launch was ended by the user.
        return LaunchExited

    # Function list.

    InLaunchFunctions = {"Drive" : Drive,
                         "DriveUltrasonic" : DriveUltrasonic,
                         "Turn" : Turn,
                         "MotorOn" : MotorOn,
                         "MotorOff" : MotorOff,
                         "Wait" : Wait}
    
    # Other functions.
    
    def Display(Self, Text):
        Self.LCD.text_pixels(Text)
        Self.LCD.update()
    
    def Button(Self, Button):
        Pressed = {"LEFT" : Self.Buttons.left,
                   "RIGHT" : Self.Buttons.right,
                   "UP" : Self.Buttons.up,
                   "DOWN" : Self.Buttons.down}
        return Pressed[Button]

def RunLaunch(Launch, Robot):
    # Cycle through the steps of the launch.
    for Step in Launch:
        StepExited = Robot.InLaunchFunctions[Step[0]](Robot, Step[1:])
        # Return true and exit the launch if the step was exited.
        if StepExited:
            return True
    # Return false if the launch was completed without being exited on any step.
    return False