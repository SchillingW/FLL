#!/usr/bin/env python3

# Returns a list representing a launch that places a tower.
def Tower(distance, angle):
    return [
    ["Drive"           , 0     ,  10 ,  distance ],
    ["Drive"           , 0     , -20 , -distance ],
    ["Turn"            , 0     ,  30 ,  angle    ],
    ["DriveUltrasonic" , angle , -20 ,  5        ],
    ]

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

# Places the tan tower.
TanTower = [
    ["Drive"           ,  0  ,  10  ,  110 ],
    ["Drive"           ,  0  , -20  , -160 ],
]

# Places the red tower.
RedTower = [
    ["Drive"           ,  0  ,  10  ,  65  ],
    ["Drive"           ,  0  , -20  , -115 ],
]

# Does all aspects of the crane mission.
Crane = [
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

# Places the blue and white towers in the black circle.
MixedTower = Tower(55, 90)

# Places the inovative architecture module in the black circle.
Architecture = Tower(45, 45)

# Flips the elevator and lowers two beams on the safety factor.
East = [
    ["Drive"            ,  0  ,  25  ,  45  ],
    ["Turn"             ,  0  , -20  , -140 ],
    ["Drive"            , -135, -20  , -101 ],
    ["Turn"             ,  0  ,  25  ,  50  ],
    ["DriveUltrasonic"  ,  50 , -20  ,  10  ],
    ["Turn"             ,  5  , -30  ,  0   ],
]

# Raises the traffic jam and starts the swing.
South = [
    ["Turn"            ,  11 ,  30  ,  90  ],
    ["Drive"           ,  90 ,  10  ,  90  ],
    ["Turn"            ,  0  , -30  ,  75  ],
    ["LineFollow"      ,        5          ],
    ["Turn"            , -10 ,  30  ,  90  ],
    ["Drive"           ,  90 ,  10  ,  20  ],
    ["Wait"            ,               1   ],
    ["DriveUltrasonic" ,  90 , -20  ,  10  ],
    ["Turn"            ,  5  , -30  ,  0   ],
]

# Places a blue module and two large modules in the tree.
TreeHouse = [
    ["Drive"            ,  0  ,  20  ,  65 ],
    ["Drive"            ,  0  , -30  , -45 ],
    ["Turn"             ,  0  ,  10  , -45 ],
    ["Drive"            ,  0  , -10  , 100 ],
    ["Turn"             ,  0  ,  30  , 180 ],
]

Launches = [TanTower, RedTower, Crane, MixedTower, Architecture, East, South, TreeHouse]
