"""
CS5800 Final Project: BSPTree
Author: Xin Qi, Yuting Xie
Other Team Members: Benjamin Johnson, Shitai Zhao
Date: July 29th, 2024
This program stores data for input triangles
"""

# points for triangle
P_0 = (1.0, 1.0)
P_1 = (7.0, 1.0)
P_2 = (7.0, 8.0)

# segments: a tuple of two points
SEGMENTS = [(P_0, P_1), (P_1, P_2), (P_2, P_0)]

# Example two
P_00 = (1.0, 1.0)
P_01 = (7.0, 1.0)
P_02 = (7.0, 8.0)
P_03 = (1.0, 8.0)
#
P_04 = (4.0, 1.0)
P_05 = (4.0, 8.0)

SEGMENTS = [
    (P_00, P_01), (P_01, P_02), (P_02, P_03), (P_03, P_00),
    (P_04, P_05),
]

CAM_POS = (6, 7)
