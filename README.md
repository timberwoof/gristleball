# gristleball
Simple Monte Carlo Simulation in Python, which I really should have called Monte Python. 

# Goals: Simplicity
Requirements for use: 
* Be able to write a mathematical evaluation in Python.

Supply: 
* sample main program with sample calculator classes
* Package that contains all the support classes

# Quick Start
Run the example with 
python3 gbIterator.py

Make a backup of exmaple.py.
Edit example.py to suit your needs. 
Run the modified file with 
python3 gbIterator.py

#Better Start
Copy example.py to MyModel.Py. 
Edit MyModel.Py to suit your needs.
In Iterator.py modify the line
from example import model
to
from MyModel import model
Run your model with 
python3 gbIterator.py

# Distribution Classes
* uniform (xmin, xmax)
* triangle (xmin, xcenter, xmax)
* gaussian (xmean, stdDev)
* etc
Each has 
* constructor with its parameters
* calculator that returns one value each time it's called

# Result Class
* constructor with parameters for name (title), x axis label, y axis label, number of buckets, x units, y units. Optionally give the expected min-max values. 
* tallier to call every time the iterator loops. If you specified the buckets, then it bins the result right away. If you did not, then it puts the result into a list. 
* grapher that creates the graph from its results. 

# Iterator Class (Main)
* calls your model class constructor
* iterator calls your model class calculator
* (if calculator didn't crash) iterator calls the results tallier
* when it's done, it calls all the talliers to create the graphs. In V1 done is after a specified number of iterations. 

# Your Class for calculator
* constructor method gets called once and calls the needed distribution constructors, one for every variable your model needs
* calculator function gets called a zillion times by the iterator. It calls the distribution functions for values, calculates the results, and returns list results of to the iterator. You should write this to be efficient. 

# Required libraries
* random
* numpy
* pyplot

# To Do
* Make the user model library a parameter to the main class. 
* Put everything else into a package or something. 
* Test for required packages and give actually helpful instructions for what to do. 
* Error handling.
