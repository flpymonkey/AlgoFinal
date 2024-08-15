"""
CS5800 Final Project: BSPTree
Author: Yuting Xie
Other Team Members: Benjamin Johnson, Shitai Zhao, Qi Xin
Date: Aug 6th, 2024
This program includes the helper functions:
cross_2d(vec_0, vec_1)
is_on_front(vec_0, vec_1)
in_on_back(vec_0, vec_1)
"""

from glm import vec2


def cross_2d(vec_0: vec2, vec_1: vec2):
    '''
    Computes the 2D cross product of two vectors.

    Args:
        vec_0 (vec2): The first vector.
        vec_1 (vec2): The second vector.

    Returns:
        float: The 2D cross product of vec_0 and vec_1.
    '''
    return vec_0.x * vec_1.y - vec_1.x * vec_0.y


def is_on_front(vec_0: vec2, vec_1: vec2):
    '''
    Determines if vec_0 is on the front side relative to vec_1.

    Args:
        vec_0 (vec2): The first vector.
        vec_1 (vec2): The second vector.

    Returns:
        True if vec_0 is on the front side relative to vec_1, False otherwise
    '''
    return vec_0.x * vec_1.y < vec_1.x * vec_0.y


def is_on_back(vec_0: vec2, vec_1: vec2):
    '''
    Determines if vec_0 is on the back side relative to vec_1.

    Args:
        vec_0 (vec2): The first vector.
        vec_1 (vec2): The second vector.

    Returns:
        True if vec_0 is on the back side relative to vec_1, False otherwise
    '''
    return not is_on_front(vec_0, vec_1)
