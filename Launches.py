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

West = [
    ["DriveUltrasonic" ,  0 ,   10  ,  65  ],
    ["DriveUltrasonic" ,  0 ,  -10  ,  5   ],
]

LargeTower = [
    ["Drive"           ,  0  ,  5   ,  5   ],
    ["DriveUltrasonic" ,  0  ,  5   ,  60  ],
    ["DriveUltrasonic" ,  0  , -20  ,  20  ],
    ["Turn"            , -20 ,  30  ,  90  ],
]

Launches = [TanTower, RedTower, West, LargeTower]
