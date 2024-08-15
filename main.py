'''
CS5800 Final Project: BSPTree
Author: Xin Qi, Yuting Xie
Other Team Members: Benjamin Johnson, Shitai Zhao
Date: Aug 9th, 2024

BSP Tree Visualization

This script demonstrates the implementation
and visualizationof a BSP tree.

To run the script, simply execute it as follows:
python main.py
'''

from settings import WIN_WIDTH, WIN_HEIGHT
from input import SEGMENTS, CAM_POS
import pyray as ray
from glm import vec2
from BSPTree import Segment, BSPTreeBuilder
from BSPTreeTraverser import BSPTreeTraverser
from view import Viewer


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


def main():
    ray.set_trace_log_level(ray.LOG_ERROR)
    ray.init_window(WIN_WIDTH, WIN_HEIGHT, 'BSP Tree')
    segment_list = create_segments(SEGMENTS)
    bsp_tree = BSPTreeBuilder(segment_list)
    cam_pos = vec2(*CAM_POS)
    bsp_traverser = BSPTreeTraverser(bsp_tree, cam_pos)
    splitted_segments = bsp_tree.segments
    viewer = Viewer(splitted_segments, bsp_tree, bsp_traverser)

    while not ray.window_should_close():
        bsp_traverser.update()
        ray.begin_drawing()
        ray.clear_background(ray.BLACK)
        viewer.draw()
        ray.end_drawing()
    ray.close_window()


if __name__ == '__main__':
    main()
