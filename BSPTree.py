"""
CS5800 Final Project: BSPTree
Author: Xin Qi, Yuting Xie
Other Team Members: Benjamin Johnson, Shitai Zhao
Date: July 29th, 2024
This program includes essental classes for BSPTree.
"""
from settings import vec2


class Segment:
    def __init__(self, point1, point2):
        """
        Params:
            point1, point2: tuple of (x, y) coordinates
        """
        self.position = vec2(point1), vec2(point2)
        self.vector = self.position[1] - self.position[0]


class BSPNode:
    def __init__(self, front=None, back=None):
        self.front = front  # front node is BSPNode
        self.back = back  # back node is BSPNode

        self.splitter_point1 = None
        self.splitter_point2 = None
        self.splitter_vector = None

        self.segment_id = None

