import graphviz
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import os

from view import Viewer

import pyray as ray

from BSPTree import *
from BSPTreeTraverser import BSPTreeTraverser
from settings import WIN_WIDTH, WIN_HEIGHT
from input import CAM_POS


# Download graphviz and add it to your libary: https://graphviz.org/download/

import os
# Can manually add graphviz to your path here
os.environ["PATH"] += os.pathsep + 'C:/Users/bencj/Downloads/windows_10_cmake_Release_Graphviz-12.0.0-win64/Graphviz-12.0.0-win64/bin'


IMG_WIDTH = 600
IMG_HEIGHT = 600


# Points

# Example one
# P_00 = (1.0, 1.0)
# P_01 = (7.0, 1.0)
# P_02 = (7.0, 8.0)
# P_03 = (1.0, 8.0)
# #
# P_04 = (5.0, 2.0)
# P_05 = (4.0, 4.0)
# P_06 = (5.0, 6.0)
# P_07 = (6.0, 4.0)

# SEGMENTS = [
#     (P_04, P_05), (P_05, P_06), (P_06, P_07), (P_07, P_04),
#     (P_00, P_01), (P_01, P_02), (P_02, P_03), (P_03, P_00),
# ]

# POINTS = [
#     P_00, P_01, P_02, P_03, P_04, P_05, P_06, P_07
# ]


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

POINTS = [
    P_00, P_01, P_02, P_03, P_04, P_05, 
]

tree = None

# Need to keep images so they dont get grabage collected: https://stackoverflow.com/questions/45668895/tkinter-tclerror-image-doesnt-exist
img = None
photoimg = None


def showimage(event):
    if os.path.exists("tree.png"):
        return os.system("tree.png") 
    else:
        return None
    
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


def add(tree, pointlist, segmentlist, lblimage):
    global img
    global photoimg

    tree.visualizetree(tree.root_node)

    img = Image.open("tree.png")

    resize = img

    # Once we have a lot of segments, we need to scale the image size to fit the screen
    if (len(SEGMENTS) > 9):
        resize = img.resize((IMG_WIDTH, IMG_HEIGHT), Image.LANCZOS)

    photoimg = ImageTk.PhotoImage(resize)
    lblimage.configure(image=photoimg)
    lblimage.image = photoimg

    updateNodeList(tree, segmentlist)
    updatePointList(pointlist)

def updatePointList(pointlist):
    pointlist.delete(0, tk.END)
    for point in POINTS:
        pointlist.insert(tk.END, point)


def updateNodeList(tree, seglist):
    seglist.delete(0, tk.END)

    root =  tree.root_node

    nodes =  getAllChilds(root)

    nodes.append(root)
    # Insert new items
    for node in nodes:
        seglist.insert(tk.END, str(node.segment_id) + " - (" + 
                    str(node.splitter_point1.x) + "," + str(node.splitter_point1.y) +
                    ") (" + str(node.splitter_point2.x) + "," + str(node.splitter_point2.y) + ")")

def getAllChilds(node):
    if node == None:
        return []

    nodes = []
    if node.front:
        nodes.append(node.front)
        nodes.extend(getAllChilds(node.front))
    if node.back:
        nodes.append(node.back)
        nodes.extend(getAllChilds(node.back))
    return nodes

def main():
    ray.set_trace_log_level(ray.LOG_ERROR)
    ray.init_window(WIN_WIDTH, WIN_HEIGHT, 'BSP Tree')
    segment_list = create_segments(SEGMENTS)
    bsp_tree = BSPTreeBuilder(segment_list)
    cam_pos = vec2(*CAM_POS)
    bsp_traverser = BSPTreeTraverser(bsp_tree, cam_pos)
    viewer = Viewer(segment_list, bsp_tree, bsp_traverser)


    root = tk.Tk()
    root.title("Binary Space Partitioning Tree")
    root.geometry("900x800")

    while not ray.window_should_close():
        bsp_traverser.update()
        ray.begin_drawing()
        ray.clear_background(ray.BLACK)
        viewer.draw()
        ray.end_drawing()


        lbl_seg = tk.Label(root,text="Segments:")
        lbl_seg.place(x=100,y=200,width=100)
        # Add a listbox to display segement details
        seglist = tk.Listbox(root)
        seglist.place(x=100,y=250,width=300, height=400)

        lbl_point = tk.Label(root,text="Points:")
        lbl_point.place(x=0,y=200,width=100)
        # Add a listbox to display point details
        pointlist = tk.Listbox(root)
        pointlist.place(x=0,y=250,width=100, height=400)

        lblimage = tk.Label(root)
        lblimage.bind("<Button-1>",showimage)
        lblimage.place(x=300,y=10,width=IMG_WIDTH,height=IMG_HEIGHT)

        add(bsp_tree, pointlist, seglist, lblimage)

        root.mainloop()

        if os.path.exists("tree.png"):
            os.remove("tree.png")
            os.remove("tree")
        
    ray.close_window()


if __name__ == '__main__':
    main()
