# gristleball
Simple Monte Carlo Simulation in Python

# Quick Start
Run the example with 
python3 gbIterator.py

Make a backup of exmaple.py . 
Edit example.py to suit your needs. 
Run the modified file with 
python3 gbIterator.py

#Better Start
Copy example.py to MyModel.Py. 
Edit MyModel.Py to suit your needs.
In Iterator.py modify the line
from example import model
ro
from MyModel import model
Run your model with 
python3 gbIterator.py

# Distribution Classes
* linear (xmin, xmax, or xmean, xdeviation, y)
* triangle (xmin, xcenter, xmax, y)
* gaussian (xmean, y, stdDev)
* poisson (…)
Each has 
* constructor with its parameters
* calculator that returns one value each time it's called

# Result Class
* constructor with parameters for name (title), x axis label, y axis label, number of buckets, x units, y units. Optionally give the expected min-max values. 
* tallier to call every time the iterator loops. If you specified the buckets, then it bins the result right away. If you did not, then it puts the result into a list. 
* grapher that creates the graph from its results. If you specified the bins, then it makes the graph directly. If you did not specify the mins then it does min-max on the list, makes the bins, and fills the bins to make the graph. 
* V1 doesn't let you specify the buckets; it just makes them in the graphing step. V2 has the optimization that you can specify the bins. 

# Iterator Class 
* constructor sets up graphing and calls your model class constructor
* iterator calls your model class calculator
* (if calculator didn't crash) iterator calls the results tallier
* when it's done, it calls all the talliers to create the graphs. In V1 done is after a specified number of iterations. 

# Your Class for calculator
* constructor method gets called once and calls the needed distribution constructors, one for every variable your model needs
* calculator function gets called a zillion times by the iterator. It calls the distribution functions for values, calculates the results, and returns list results of to the iterator. You should write this to be efficient. 

# Required libraries
random
numpy
pyplot

# Goals: Simplicity
Requirements for use: 
Be able to write a mathematical evaluation in Python

Supply: sample main program with sample calculator class
Package that contains all the support classes
