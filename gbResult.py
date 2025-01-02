"""Result class for Gristleball"""
# Instantiate one of these for every result you expect from your model.
from matplotlib import pyplot as plt  # python3 -m pip install -U matplotlib
import math

class result:
    def __init__(self, title, labelX, num_bins):
        print (f"gbResult init({title}, {labelX}, {num_bins})")
        self.title = title
        self.labelX = labelX
        self.num_bins = num_bins
        self.results = []

    def put(self, value):
        """tally up one result from the mathematical model you wrote"""
        self.results.append(value)

    def plot(self):
        """create a graph of the histogram for this result"""
        # calculates the bin sizes and distributes the accumulated baliues into them
        # then calls pyplot to make a graph.
        print('gbResult plot')

        # create the graph
        plt.clf()
        plt.cla()
        plt.title(self.title)
        plt.xlabel(self.labelX)
        plt.ylabel('Likelihood')
        plt.hist(x=self.results, bins=self.num_bins, histtype='bar') # , color=colors
        plt.show()
        # print("gbResult plot saving plot to histogram")
        #fig.savefig("histogram", dpi=fig.dpi)
