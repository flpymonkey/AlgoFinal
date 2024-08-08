"""
CS5800 Final Project: BSPTree
Author: Xin Qi, Yuting Xie
Other Team Members: Benjamin Johnson, Shitai Zhao
Date: July 29th, 2024
This program stores data for input triangles
"""


# points
P_00 = (1.0, 1.0)
P_01 = (7.0, 1.0)
P_02 = (7.0, 8.0)
P_03 = (1.0, 8.0)

P_04 = (5.0, 2.0)
P_05 = (4.0, 4.0)
P_06 = (5.0, 6.0)
P_07 = (6.0, 4.0)

P_08 = (1.8, 1.8)
P_09 = (1.8, 4.2)
P_10 = (3.5, 4.2)
P_11 = (3.5, 1.8)

P_12 = (1.5, 5.5)
P_13 = (1.5, 6.5)
P_14 = (2.0, 6.5)
P_15 = (2.0, 5.5)

# segments: a tuple of two points
SEGMENTS = [(P_00, P_01), (P_01, P_02), (P_02, P_03), (P_03, P_00),
            (P_04, P_05), (P_05, P_06), (P_06, P_07), (P_07, P_04),
            (P_08, P_09), (P_09, P_10), (P_10, P_11), (P_11, P_08),
            (P_12, P_13), (P_13, P_14), (P_14, P_15), (P_15, P_12)]

CAM_POS = (6, 7)
