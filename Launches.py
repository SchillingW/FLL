#!/usr/bin/env python3

# Key a (path):
#
#  1 - angle
#  2 - turn radius
#  3 - motor id

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
#   ["Drive"           ,  1  ,  1  ,  1  ],
#   ["DriveUltrasonic" ,  1  ,  1  ,  2  ],
#   ["Turn"            ,  2  ,  2  ,  3  ],
#   ["LineFollow"      ,        1        ],
#   ["MotorOn"         ,  3  ,  3        ],
#   ["MotorOff"        ,  3              ],
#   ["Wait"            ,              4  ],
# ]

TanTower = [
    ["Drive"           ,  0  ,  10  ,  110 ],
    ["Drive"           ,  0  , -20  , -160 ],
]

RedTower = [
    ["Drive"           ,  0  ,  10  ,  65  ],
    ["Drive"           ,  0  , -20  , -115 ],
]

West = [
    ["DriveUltrasonic" ,  0  ,  10  ,  10  ],
    ["Turn"            ,  0  ,  30  ,  90  ],
    ["DriveUltrasonic" ,  90 ,  10  ,  57  ],
    ["Turn"            ,  0  , -30  ,  0   ],
    ["DriveUltrasonic" ,  0  ,  10  ,  60  ],
    ["DriveUltrasonic" ,  0  , -5   ,  50  ],
    ["DriveUltrasonic" ,  0  ,  5   ,  65  ],
    ["Wait"            ,  2                ],
    ["DriveUltrasonic" ,  0  , -20  ,  50  ],
    ["Turn"            ,  0  ,  30  ,  90  ],
    ["DriveUltrasonic" ,  90 , -20  ,  10  ],
    ["Turn"            ,  5  , -30  ,  0   ],
]

LargeTower = [
    ["Drive"           ,  0  ,  5   ,  5   ],
    ["DriveUltrasonic" ,  0  ,  5   ,  60  ],
    ["DriveUltrasonic" ,  0  , -20  ,  20  ],
    ["Turn"            , -20 ,  30  ,  90  ],
]

SafetyFactor = [
    ["Drive"            ,  0  ,  25  ,  45  ],
    ["Turn"             ,  0  , -20  , -140 ],
    ["Drive"            , -135, -20  , -101 ],
    ["Turn"             ,  0  ,  25  ,  50  ],
    ["DriveUltrasonic"  ,  50 , -20  ,  10  ],
    ["Turn"             ,  5  , -30  ,  0   ],
]

TreeHouse = [
    ["Drive"            ,  0  ,  20  ,  65 ],
    ["Drive"            ,  0  , -30  , -45 ],
    ["Turn"             ,  0  ,  10  , -45 ],
    ["Drive"            ,  0  , -10  , 100 ],
    ["Turn"             ,  0  ,  30  , 180 ],
]

South = [
    ["Turn"            ,  11 ,  30  ,  90  ],
    ["MotorOn"         ,  1  ,  .11        ],
    ["Drive"           ,  90 ,  10  ,  90  ],
    ["MotorOff"        ,  1                ],
    ["Turn"            ,  0  , -30  ,  75  ],
    ["LineFollow"      ,        5          ],
    ["Turn"            , -10 ,  30  ,  90  ],
    ["MotorOn"         ,  1  , -.5         ],
    ["Drive"           ,  90 ,  10  ,  20  ],
    ["MotorOff"        ,  1                ],
    ["Wait"            ,               1   ],
    ["DriveUltrasonic" ,  90 , -20  ,  10  ],
    ["Turn"            ,  5  , -30  ,  0   ],
]

Launches = [TanTower, RedTower, West, LargeTower, SafetyFactor, TreeHouse, South]
