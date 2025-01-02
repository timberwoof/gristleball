"""Result class for Gristleball"""
# Instantiate one of these for every result you expect from your model.
from matplotlib import pyplot as plt  # python3 -m pip install -U matplotlib
import math

class result:
    def __init__(self, title, labelX, labelY, xMin, xMax, num_bins):
        print (f"gbResult init({title}, {labelX}, {labelY}, {xMin}, {xMax}, {num_bins})")
        self.title = title
        self.labelX = labelX
        self.labelY = labelY
        self.xMin = xMin
        self.xMax = xMax
        self.num_bins = num_bins
        self.bins = [0] * num_bins

    def put(self, value):
        """tally up one result from the mathematical model you wrote"""
        bin = math.floor((value - self.xMin) / self.xMax * self.num_bins)
        print(f"result.put({value}) into bin {bin}")
        self.bins[bin] = self.bins[bin] + 1

    def plot(self):
        """create a graph of the histogram for this result"""
        print('gbResult plot')
        plt.clf()
        plt.cla()
        plt.title(self.title)
        plt.xlabel(self.labelX)
        plt.ylabel(self.labelY)
        plt.hist(x=self.bins, bins=self.num_bins, histtype='bar') # , color=colors
        plt.show()
        # print("gbResult plot saving plot to histogram")
        #fig.savefig("histogram", dpi=fig.dpi)
