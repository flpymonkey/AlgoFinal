"""
CS5800 Final Project: BSPTree
Author: Xin Qi, Yuting Xie
Other Team Members: Benjamin Johnson, Shitai Zhao
Date: July 29th, 2024
This program stores data for input triangles
"""


# Example one

# Create all the points for the line segments
P_00 = (1.0, 1.0)
P_01 = (7.0, 1.0)
P_02 = (7.0, 8.0)
P_03 = (1.0, 8.0)
#
P_04 = (5.0, 2.0)
P_05 = (4.0, 4.0)
P_06 = (5.0, 6.0)
P_07 = (6.0, 4.0)

# Create all the line segmeents by connecting pairs of points listed above
# This will create a large square from the first four points,
# and a small square fro mthe last four points.
SEGMENTS = [
    (P_04, P_05), (P_05, P_06), (P_06, P_07), (P_07, P_04),
    (P_00, P_01), (P_01, P_02), (P_02, P_03), (P_03, P_00),
]

# Add all the points to a list
POINTS = [
    P_00, P_01, P_02, P_03, P_04, P_05, P_06, P_07
]

# Define the camera position
CAM_POS = (6, 7)
