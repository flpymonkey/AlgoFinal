import graphviz
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import os

from BSPTree import *

# Download graphviz and add it to your libary: https://graphviz.org/download/

import os
# Can manually add graphviz to your path here
os.environ["PATH"] += os.pathsep + 'C:/Users/bencj/Downloads/windows_10_cmake_Release_Graphviz-12.0.0-win64/Graphviz-12.0.0-win64/bin'


IMG_WIDTH = 600
IMG_HEIGHT = 600

POINTS = []

SEGMENTS = []
tree = None

# Need to keep images so they dont get grabage collected: https://stackoverflow.com/questions/45668895/tkinter-tclerror-image-doesnt-exist
img = None
photoimg = None

def add():
    global tree
    global SEGMENTS
    global img
    global photoimg
    p1 = (int(txtvalue1_1.get()), int(txtvalue1_2.get()))
    p2 = (int(txtvalue2_1.get()), int(txtvalue2_2.get()))

    # See if point is already in points
    contains_p1 = False
    contains_p2 = False
    for point in POINTS:
        if point[0] == p1[0] and point[1] == p1[1]:
            contains_p1 = True
    
    for point in POINTS:
        if point[0] == p2[0] and point[1] == p2[1]:
            contains_p2 = True

    if not contains_p1:
        POINTS.append(p1)
    if not contains_p2:
        POINTS.append(p2)

    # Build triangle segments
    seg1 = Segment(p1, p2)

    SEGMENTS.append(seg1)


    # Add the first node
    tree = BSPTreeBuilder(SEGMENTS)

    tree.visualizetree(tree.root_node)
    img = Image.open("tree.png")

    resize = img

    # Once we have a lot of segments, we need to scale the image size to fit the screen
    if (len(SEGMENTS) > 9):
        resize = img.resize((IMG_WIDTH, IMG_HEIGHT), Image.LANCZOS)

    photoimg = ImageTk.PhotoImage(resize)
    lblimage.configure(image=photoimg)
    lblimage.image = photoimg

    updateNodeList()
    updatePointList()

def updatePointList():
    listbox2.delete(0, tk.END)
    for point in POINTS:
        listbox2.insert(tk.END, point)


def updateNodeList():
    listbox.delete(0, tk.END)

    root = tree.root_node

    nodes = tree.getAllChilds(root)

    nodes.append(root)
    # Insert new items
    for node in nodes:
        listbox.insert(tk.END, str(node.segment_id) + " - (" + 
                       str(node.splitter_point1.x) + "," + str(node.splitter_point1.y) +
                       ") (" + str(node.splitter_point2.x) + "," + str(node.splitter_point2.y) + ")")

def showimage(event):
    if os.path.exists("tree.png"):
        return os.system("tree.png") 
    else:
        return None

if __name__ == "__main__":

    root = tk.Tk()
    root.title("Binary Space Partitioning Tree")
    root.geometry("900x800")

    lblvalue = tk.Label(root,text="Data point 1 (x, y):")
    lblvalue.place(x=50,y=50,width=100)

    txtvalue1_1 = tk.Entry(root)
    txtvalue1_1.place(x=150,y=50,width=100)

    txtvalue1_2 = tk.Entry(root)
    txtvalue1_2.place(x=200,y=50,width=100)

    lblvalue2 = tk.Label(root,text="Data point 2 (x, y):")
    lblvalue2.place(x=50,y=100,width=100)

    txtvalue2_1 = tk.Entry(root)
    txtvalue2_1.place(x=150,y=100,width=100)

    txtvalue2_2 = tk.Entry(root)
    txtvalue2_2.place(x=200,y=100,width=100)

    btnadd = tk.Button(root,text="Add",command=add)
    btnadd.place(x=50,y=150,width=100)

    lbl_seg = tk.Label(root,text="Segments:")
    lbl_seg.place(x=100,y=200,width=100)
    # Add a listbox to display segement details
    listbox = tk.Listbox(root)
    listbox.place(x=100,y=250,width=300, height=400)

    lbl_point = tk.Label(root,text="Points:")
    lbl_point.place(x=0,y=200,width=100)
    # Add a listbox to display point details
    listbox2 = tk.Listbox(root)
    listbox2.place(x=0,y=250,width=100, height=400)

    lblimage = tk.Label(root)
    lblimage.bind("<Button-1>",showimage)
    lblimage.place(x=300,y=10,width=IMG_WIDTH,height=IMG_HEIGHT)
    root.mainloop()

    if os.path.exists("tree.png"):
       os.remove("tree.png")
       os.remove("tree")