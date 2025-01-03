# gristleball
Simple Monte Carlo Simulation in Python, which I really should have called Monte Python. 
Reference: "Crystal Ball Version 3.0: Forecasting and Risk Analysis for Sporeadsheet Users", Decisioneering, Inc, 1993

# Goals: Simplicity
Requirements for use: 
* You must be able to write your mathematical model as Python methods.

This project will provide:
* Python classes that demonstrate mathematical models to analyze. 
* Package that contains all the support classes

# Compatibility and Pricing
* Compatible with all platforms that can run Python 3, numpy, and Pyplot: Linux, MacOS, and Widnows.
* Free as in Beer. 

# Quick Start
Run the example with 
python3 gbIterator.py

Make a backup of exmaple.py.
Edit example.py to suit your needs. 
Run the modified file with 
python3 gbIterator.py

# Better Start
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
* constructor with parameters
* calculator that returns one value each time it's called

# Your Class for calculator
* Constructor method __init__ gets called once and calls the needed distribution constructors, one for every variable your model needs.
* Calculator function calculate() gets called a zillion times by the iterator. It calls the distribution functions for values, calculates the results, and put them into the result class. You should write this to be efficient. 

# Result Class
* constructor with parameters for name (title), number of bins, x axis label 
* tallier that the model calls every time it is called by the iterator
* grapher that creates the graphs from its results

# Iterator Class (Monte)
* This is the main program. Run this. 
* It calls your model class constructor.
* It repeatedly calls your model class calculator.
* When it's done, it calls the result classes to create the graphs. 

# Required libraries
* random
* numpy: pip install numpy
* matplotlib pyplot:  pip install matplotlib

# To Do
* Make the user model class name a parameter to the main class. 
* Put everything else into a package or something. 
* At runtime test for required packages and give actually helpful instructions for what to do. 
* Error handling.
* More distribution types.
