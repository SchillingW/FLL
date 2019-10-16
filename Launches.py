#!/usr/bin/env python3
L1 = [
    ["Drive", 10, 100]
]

L2 = [
    ["DriveUltrasonic", 20, 100]
]

L3 = [
    ["Turn", 10, 18, 180]
]

L4 = [
    ["MotorOn", 1, 1],
    ["Wait", 2],
    ["MotorOn", 0, -1],
    ["Wait", 3],
    ["MotorOff", 0],
    ["MotorOff", 1]
]

Launches = [L1, L2, L3, L4]