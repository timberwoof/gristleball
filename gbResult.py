"""Result class for Gristleball"""
# This object knows about only one set of results.
# Instantiate one of these for every result you expect from your model.
from matplotlib import pyplot  # python3 -m pip install -U matplotlib
import math

class result:
    def __init__(self, title, labelX, num_bins=100):
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
        print(f'gbResult plot {self.title}')

        # create the graph
        pyplot.clf()
        pyplot.cla()
        pyplot.title(self.title)
        pyplot.xlabel(self.labelX)
        pyplot.ylabel('Probability')
        pyplot.hist(x=self.results, bins=self.num_bins, histtype='bar', density=True) # , color=colors
        print("gbResult plot saving plot to histogram")
        fig = pyplot.gcf()
        fig.savefig(f"Monte Carlo Analysis for {self.title}.png")
        pyplot.show()

if __name__ == "__main__":
    print("Don't run this. Run python3 monte instead.")