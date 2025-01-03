"""Gristleball Iterator"""
#  The main program of Gristleball.

# *** this needs to import your specific model class
# *** Modify "example" in this line to point to your model
# *** Run this file:
# python3 gbIterator.py
from test_binomial import model

# The rest of this code is usable as-is.
from gbResult import result

def main():
    print("main")
    # This is where your mathematical model gets incorporated.
    theModel = model() # parameters are set up in user's __init__
    i = 0
    while i < theModel.iterations:
        # Here's where your model gets called and the result tallied.
        theModel.calculate()
        i = i + 1

    # And here's where the graphs get made
    for result in theModel.results:
        result.plot()

if __name__ == "__main__":
    main()