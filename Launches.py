#!/usr/bin/env python3

# Key a (path):
#
#  1 - turn radius
#  2 - motor id

# Key b (speed):
#
#  1 - cm/sec
#  2 - deg/sec
#  3 - rot/sec

# Key c (target):
#
#  1 - drive centimeters
#  2 - target centimeters
#  3 - target degrees
#  4 - seconds

#   ["MoveType"        ,  a  ,  b  ,  c  ],
#
# LaunchName = [
#   ["Drive"           ,     ,  1  ,  1  ],
#   ["DriveUltrasonic" ,     ,  1  ,  2  ],
#   ["Turn"            ,  1  ,  2  ,  3  ],
#   ["LineFollow"      ,     ,  1  ,     ],
#   ["MotorOn"         ,  2  ,  3  ,     ],
#   ["MotorOff"        ,  2  ,     ,     ],
#   ["Wait"            ,     ,     ,  4  ],
# ]

L1 = [
    ["DriveUltrasonic" ,        5  ,  60 ],
    ["DriveUltrasonic" ,       -10 ,  20 ],
    ["Turn"            , -20 ,  30 ,  90 ],
]

L2 = [
    ["Turn"            ,  13 ,  30 ,  90 ],
    ["Drive"           ,        10 ,  90 ],
    ["Turn"            ,  0  , -30 ,  45 ],
    ["LineFollow"      ,        5        ],
    ["Turn"            , -5  ,  30 ,  90 ],
    ["Drive"           ,        10 ,  15 ],
    ["Drive"           ,       -10 , -15 ],
    ["Turn"            ,  0  ,  9  ,  90 ],
    ["Turn"            ,  0  , -9  ,  90 ],
    ["DriveUltrasonic" ,       -20 ,  15 ],
    ["Turn"            ,  15 , -30 ,  0  ],
]

L3 = [
]

L4 = [
]

Launches = [L1, L2, L3, L4]
