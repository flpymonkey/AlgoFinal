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

SEGMENTS = []
tree = None

def add():
    global tree
    global SEGMENTS
    p1 = (int(txtvalue1_1.get()), int(txtvalue1_2.get()))
    p2 = (int(txtvalue2_1.get()), int(txtvalue2_2.get()))
    p3 = (int(txtvalue3_1.get()), int(txtvalue3_2.get()))

    # Build triangle segments
    seg1 = Segment(p1, p2)
    
    seg2 = Segment(p2, p3)

    seg3 = Segment(p3, p1)

    SEGMENTS.append(seg1)
    SEGMENTS.append(seg2)
    SEGMENTS.append(seg3)


    # Add the first node
    tree = BSPTreeBuilder(SEGMENTS)

    tree.visualizetree(tree.root_node)
    img = ImageTk.PhotoImage(Image.open("tree.png"))
    lblimage.configure(image=img)
    lblimage.image = img

    updateNodeList()

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
    os.system("tree.png") if os.path.exists("tree.png") else None

if __name__ == "__main__":

    root = tk.Tk()
    root.title("Binary Space Partitioning")
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

    lblvalue3 = tk.Label(root,text="Data point 3 (x, y):")
    lblvalue3.place(x=50,y=150,width=100)

    txtvalue3_1 = tk.Entry(root)
    txtvalue3_1.place(x=150,y=150,width=100)

    txtvalue3_2 = tk.Entry(root)
    txtvalue3_2.place(x=200,y=150,width=100)

    btnadd = tk.Button(root,text="Add",command=add)
    btnadd.place(x=50,y=200,width=100)

    # Add a listbox to display node details
    listbox = tk.Listbox(root)
    listbox.place(x=50,y=250,width=300, height=400)

    lblimage = tk.Label(root)
    lblimage.bind("<Button-1>",showimage)
    lblimage.place(x=300,y=10,width=600,height=600)
    root.mainloop()

    if os.path.exists("tree.png"):
       os.remove("tree.png")
       os.remove("tree")