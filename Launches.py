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
    ["Turn"            ,  13 ,  30 ,  90 ],
    ["Drive"           ,        10 ,  90 ],
    ["Turn"            ,  0  , -30 ,  45 ],
    ["LineFollow"      ,        10       ],
    ["Turn"            , -5  ,  30 ,  90 ],
    ["Drive"           ,        10 ,  15 ],
    ["DriveUltrasonic" ,       -20 ,  40 ],
    ["Turn"            ,  10 , -30 ,  0  ],
]

L2 = [
]

L3 = [
]

L4 = [
]

Launches = [L1, L2, L3, L4]
