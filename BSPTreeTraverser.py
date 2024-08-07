"""
CS5800 Final Project: BSPTree
Author: Yuting Xie
Other Team Members: Benjamin Johnson, Shitai Zhao, Qi Xin
Date: Aug 6th, 2024
This program includes essental classes for BSPTree.
"""

from BSPTree import Segment, BSPTreeBuilder, BSPNode
from glm import vec2
from helperfunctions import is_on_front


def create_segments(raw_segment):
    '''
    Converts a list of segment position pairs into a list of Segment objects
    Args:
        segment_positions:
        A list of tuples containing start and end points of segments
    Returns:
        A list of Segment objects created from the given position pairs
    '''
    segments = []
    for (p0, p1) in raw_segment:
        segments.append(Segment(p0, p1))
    return segments


class BSPTreeTraverser:
    '''
    Traversing a Binary Space Partitioning (BSP) tree and determining
    the order in which segments should be drawn based on the camera position

    Attributes:
        root_node (BSPNode): The root node of the BSP tree.
        segments (list[Segment]): The list of segments used in the BSP tree.
        cam_pos (vec2): The current position of the camera.
        seg_ids_to_draw (list[int]):
        A list of segment IDs representing the order
        in which segments should be drawn.

    Methods:
        update():
        Clears the current drawing order and traverses the BSP tree
        to update the drawing order based on the current camera position.
        traverse(node):
        Recursively traverses the BSP tree from the given node,
        determining the drawing order of segments based on
        their relative position to the camera.
    '''
    def __init__(self, BSPTree: BSPTreeBuilder, cam_pos: vec2):
        '''
        Initializes the BSPTreeTraverser
        with the given BSP tree and camera position

        Args:
            BSPTree (BSPTree): The BSP tree to be traversed
            cam_pos (vec2): The initial position of the camera
        '''
        self.root_node = BSPTree.root_node
        self.segments = BSPTree.segments
        self.cam_pos = cam_pos
        self.seg_ids_to_draw = []

    def update(self):
        '''
        Updates the order of segments to be drawn
        by clearing the current list and
        traversing the BSP tree from the root node.
        '''
        self.seg_ids_to_draw.clear()
        self.traverse(self.root_node)

    def traverse(self, node: BSPNode):
        '''
        Recursively traverses the BSP tree from the given node,
        determining the drawing order of segments based on
        their relative position to the camera
        Args:
            node (BSPNode): The current node in the BSP tree
        Returns:
            None
        '''
        if node is None:
            return
        # Determine if the camera is on the front of the node's splitter
        on_front = is_on_front(self.cam_pos - node.splitter_point1,
                               node.splitter_vector)
        if on_front:
            self.traverse(node.front)
            self.seg_ids_to_draw.append(node.segment_id)
            self.traverse(node.back)
        else:
            self.traverse(node.back)
            self.seg_ids_to_draw.append(node.segment_id)
            self.traverse(node.front)
