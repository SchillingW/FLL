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

South = [
    ["Turn"            ,  11 ,  30  ,  90  ],
    ["MotorOn"         ,  1  ,  0.1        ],
    ["Drive"           ,  90 ,  10  ,  90  ],
    ["MotorOff"        ,  1                ],
    ["Turn"            ,  0  , -30  ,  60  ],
    ["LineFollow"      ,        5          ],
    ["Turn"            , -5  ,  30  ,  90  ],
    ["MotorOn"         ,  1  , -0.5        ],
    ["Drive"           ,  90 ,  10  ,  15  ],
    ["MotorOff"        ,  1                ],
    ["DriveUltrasonic" ,  90 , -20  ,  18  ],
    ["Turn"            ,  15 , -30  ,  0   ],
]

LargeTower = [
    ["Drive"           ,  0  ,  5   ,  5   ],
    ["DriveUltrasonic" ,  0  ,  5   ,  60  ],
    ["DriveUltrasonic" ,  0  , -20  ,  20  ],
    ["Turn"            , -20 ,  30  ,  90  ],
]

RedTower = [
    ["Drive"           ,  0  ,  10  ,  103 ],
    ["Drive"           ,  0  , -10  , -103 ],
]

TanTower = [
    ["Drive"           ,  0  ,  10  ,  65  ],
    ["Drive"           ,  0  , -10  , -65  ],
]

Bridge = [
    ["Drive"           ,  0  ,  50  ,  65  ],
]

Launches = [South, LargeTower, RedTower, TanTower, Bridge]
