"""
CS5800 Final Project: BSPTree
Author: Xin Qi, Yuting Xie
Other Team Members: Benjamin Johnson, Shitai Zhao
Date: July 29th, 2024
This program includes essental classes for BSPTree.
"""
from settings import vec2, EPS
from copy import copy
from helperfunctions import cross_2d


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


class BSPTreeBuilder:
    def __init__(self, raw_segments):
        self.raw_segments = raw_segments
        #
        self.root_node = BSPNode()
        #
        self.segments = []  # segments created during BSP tree creation
        self.seg_id = 0

        self.num_front, self.num_back, self.num_splits = 0, 0, 0
        self.build_bsp_tree(self.root_node, self.raw_segments)

        print('num_front:', self.num_front)
        print('num_back:', self.num_back)
        print('num_splits', self.num_splits)

    def split_space(self, node: BSPNode, input_segments: list[Segment]):
        '''
        Splits the input segments into front and back lists
        based on the splitter segment

        This method is part of the BSP tree construction process.
        It takes a list of segments and splits them into two lists:
        one containing segments in front of the splitter segment and
        one containing segments behind the splitter segment.
        The splitter segment is chosen as the first segment in the input list.

        This method also updates the BSP tree node
        with the splitter segment information,
        assigns a unique ID to each segment as it is added to the tree.

        Args:
            node (BSPNode): The current node in the BSP tree.
            input_segments (list[Segment]): A list of segments to be split.

        Returns:
            tuple: A tuple containing two lists:
                - front_segs (list[Segment]):
                    Segments in front of the splitter
                - back_segs (list[Segment]):
                    Segments behind the splitter
        '''
        # Select the first segment as the splitter segment
        splitter_seg = input_segments[0]
        splitter_pos = splitter_seg.pos
        splitter_vec = splitter_seg.vector

        # Store the splitter's vector and positions in the current node
        node.splitter_vec = splitter_vec
        node.splitter_p0 = splitter_pos[0]
        node.splitter_p1 = splitter_pos[1]

        # Initialize lists to hold segments
        # in front of and behind the splitter segment
        front_segs, back_segs = [], []

        # Iterate over the rest of the input segments
        for segment in input_segments[1:]:
            segment_start = segment.pos[0]
            segment_end = segment.pos[1]
            segment_vector = segment.vector

            # Compute the numerator and denominator
            # for the intersection calculation
            numerator = cross_2d((segment_start - splitter_pos[0]),
                                 splitter_vec)
            denominator = cross_2d(splitter_vec, segment_vector)

            # if the denominator is zero the lines are parallel
            denominator_is_zero = abs(denominator) < EPS

            # if they are parallel and the numerator is zero,
            # segments are collinear
            numerator_is_zero = abs(numerator) < EPS
            # If segments are collinear,
            # add the segment to the front segments list
            if denominator_is_zero and numerator_is_zero:
                front_segs.append(segment)
                continue

            if not denominator_is_zero:
                # intersection is the point on a line segment
                # where the line divides it
                intersection = numerator / denominator

                # segments that are not parallel and t is in (0,1)
                # should be divided
                if 0.0 < intersection < 1.0:
                    self.num_splits += 1
                    # If the intersection point lies within the segment,
                    # split the segment
                    intersection_point = (segment_start
                                          + intersection * segment_vector)

                    # Create two new segments at the intersection point
                    r_segment = copy(segment)
                    r_segment.pos = segment_start, intersection_point
                    r_segment.vector = r_segment.pos[1] - r_segment.pos[0]

                    l_segment = copy(segment)
                    l_segment.pos = intersection_point, segment_end
                    l_segment.vector = l_segment.pos[1] - l_segment.pos[0]

                    # Ensure correct front and back assignment by swapping
                    if numerator > 0:
                        l_segment, r_segment = r_segment, l_segment

                    # Add the new segments to the front and back segments lists
                    front_segs.append(r_segment)
                    back_segs.append(l_segment)
                    continue

            # Assign the segment to the front or back list
            # based on its relative position to the splitter
            if numerator < 0 or (numerator_is_zero and denominator > 0):
                front_segs.append(segment)
            elif numerator > 0 or (numerator_is_zero and denominator < 0):
                back_segs.append(segment)

        # Add the splitter segment to the BSP tree node
        self.add_segment(splitter_seg, node)
        return front_segs, back_segs

    def add_segment(self, splitter_seg: Segment, node: BSPNode):
        '''
        Adds a splitter segment to the list of segments,
        Then updates the current BSP node with the segment's ID.

        keep track of the segments that are used to split the space.
        It adds the given splitter segment to the list of segments and
        assigns a unique segment ID to the current BSP node.
        The segment ID counter is then incremented for the next segment.

        Args:
            splitter_seg (Segment): The segment used to split the space.
            node (BSPNode): The current node in the BSP tree.
        '''
        # Add the splitter segment to the list of segments
        self.segments.append(splitter_seg)
        # Assign the current segment ID to the node's segment_id attribute
        node.segment_id = self.seg_id
        # Increment the segment ID counter for the next segment
        self.seg_id += 1

    def build_bsp_tree(self, node: BSPNode, input_segments: list[Segment]):
        '''
        Recursively builds the BSP tree
        by splitting input segments into front and back lists.

        Recursively divides the input segments into two lists (front and back)
        based on their relative position to a splitter segment.
        The splitter segment is chosen as the first segment in the input list.
        The method updates the current node with the splitter segment
        and creates child nodes for the front and back spaces,
        continuing the process until no segments are left to process.

        Args:
            node (BSPNode): The current node in the BSP tree.
            input_segments (list[Segment]): A list of segments to be processed.
        '''
        # Base case:
        # If there are no segments to process,
        # return None (this branch is a leaf node)
        if not input_segments:
            return None

        # Split the input segments into front and back lists
        # using the first segment as the splitter
        front_segs, back_segs = self.split_space(node, input_segments)

        # If there are segments in the back list,
        # create a back child node and recurse
        if back_segs:
            self.num_back += 1
            # creates new BSPNode and assigns it to the back of current node
            node.back = BSPNode()
            self.build_bsp_tree(node.back, back_segs)

        # If there are segments in the front list,
        # create a front child node and recurse
        if front_segs:
            self.num_front += 1
            # creates new BSPNode and assigns it to the front of current node
            node.front = BSPNode()
            self.build_bsp_tree(node.front, front_segs)
