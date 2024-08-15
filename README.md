## AlgoFinal
GitHub Link: https://github.com/flpymonkey/AlgoFinal

### Installation instructions:

Download graphviz and add it to your libary: https://graphviz.org/download/
Ensure the library is added to your path, or manually add it in the ui.py file.

If you get the following error:
"graphviz.backend.execute.ExecutableNotFound: failed to execute WindowsPath('dot'), make sure the Graphviz executables are on your systems' PATH". 
Then your path is most likely not set properly, and you need to manually set it.

Note, you need to manually install this seperatly on your computer in addition to installing the pip python library below. There are three files which requires a manual set-up: ui_points.py, ui_shape_view.py and ui_triangle.py.

If you have this error:

AttributeError: module 'pyray' has no attribute 'ORANGE'

Try to uninstall pyray and then reinstall. This is likely due to the wrong installed version of pyray.

### Python packages:

pip install graphvizgi

pip install PyGLM

pip install tkinter

pip install pyray

You can then confirm that everything is working properly by running the following command and seeing if the app runs:

python ui_shape_view.py

### How to run the algorithm
python main.py

### How to change input
You can add and update points and segements in input.py

### How to run the visualization tools
Interactive Tree Builder:

python ui_points.py

Only show the shape view:

python main.py


### How to time the algorithm
python timing.py
