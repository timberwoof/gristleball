"""Random distributions for Gristleball"""
# Each of these provides one distribution types to feed your model.
# You can instantiate as many of these as you need to.
# You can add new distribution types to his file.
import random
import numpy

class linear:
    def __init__(self, xmin=0, xmax=1):
        print(f'initializing gbLinear(xmin={xmin}, max={xmax})')
        self.xmin = xmin
        self.xmax = xmax

    def value(self):
        return random.uniform(self.xmin, self.xmax)

class triangular:
    def __init__(self, low=0, mode=0.5, high=1):
        print(f'initializing gbLinear(low={low}, mode={mode}, high={high})')
        self.low = low
        self.mode = mode
        self.high = high

    def value(self):
        return random.triangular(self.low, self.high, self.mode)

class binomial:
    def __init__(self, prob=0.5, trials=100):
        print(f'initializing gbBinomial(prob={prob}, trials={trials})')
        self.prob = prob
        self.trials = trials

    def value(self):
        return numpy.random.binomial(self.trials, self.prob)

class custom: # *** not implemented
    def __init__(self, prob=1):
        self.prob = prob

    def value(self):
        return self.prob;

class normal:
    def __init__(self, mean, stdDev):
        print(f'initializing gbNormal(mean={mean}, stdDev={stdDev})')
        self.mean = mean
        self.stdDev = stdDev

    def value(self):
        return numpy.random.normal(self.mean, self.stdDev)

if __name__ == "__main__":
    print("Don't run this. Run gbIterator instead.")