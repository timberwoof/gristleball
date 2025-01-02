"""Random distributions for Gristleball"""
# Each of these provides one distribution types to feed your model.
# You can instantiate as many of these as you need to.
# You can add new distribution types to his file.
import random
import numpy

class uniform:
    def __init__(self, xmin=0, xmax=1):
        print(f'initializing uniform(xmin={xmin}, max={xmax})')
        self.xmin = xmin
        self.xmax = xmax

    def value(self):
        return random.uniform(self.xmin, self.xmax)

class triangular:
    def __init__(self, low=0, mode=0.5, high=1):
        print(f'initializing triangular(low={low}, mode={mode}, high={high})')
        self.low = low
        self.mode = mode
        self.high = high

    def value(self):
        return random.triangular(self.low, self.high, self.mode)

class binomial:
    def __init__(self, prob=0.5, trials=100):
        print(f'initializing binomial(prob={prob}, trials={trials})')
        self.prob = prob
        self.trials = trials

    def value(self):
        return numpy.random.binomial(self.trials, self.prob)

class custom:
    # Custom Distribution is a combination of one or more uniform distribtions.
    # Each block is defined by its min, max, and probability.
    # The min and max values live on the same X axis for all the blocks.
    # The Probability values are scaled relatively between the blocks.
    # The data structure looks like [[0.0, 0.05, 0.75], [-0.15, -0.05, 0.25]]
    # The first two parameters are the limits for this range.
    # The third parameter Prob is the probability that the value will be in this range.

    def __init__(self, prob_list):
        # The parameters given by the user are somehat flexible so we do some cleanup.
        print(f'initializing custom({prob_list})')

        # Normalize the probabilities for each range so they add up to 1.0.
        # Calculate the amount by which to multiply each blocks'
        # probability so we can normalize them to sum up to 1
        probs_sum = 0
        for a_block in prob_list:
            x1, x2, prob = a_block
            probs_sum = probs_sum + prob
        normalize_factor = 1.0 / probs_sum

        # Now normalize each block's probability
        # and store them in a new list with probability ranges
        self.normalized = []
        min = 0
        max = 0
        for a_block in prob_list:
            x1, x2, prob = a_block
            normalized = prob * normalize_factor
            max = max + normalized
            self.normalized.append([x1, x2, min, max])
            min = max

        # Now each row has the min and max values and the threshold for picking it
        # We don't care what order the blocks are in.
        print(f'done initializing custom({self.normalized})')

    def value(self):
        # Each block is normalized for relative probability with the otehrs.
        # Each is associated with its threshold values for getting picked.
        selector = random.uniform(0.0, 1.0)
        for a_block in self.normalized:
            x1, x2, min, max = a_block
            if min <= selector and selector < max:
                xmin = x1
                xmax = x2
            # If you have to optimize this selection to speed this up,
            # then you should rewrite this whole thing in C.
        return random.uniform(xmin, xmax)

class normal:
    def __init__(self, mean, stdDev):
        print(f'initializing normal(mean={mean}, stdDev={stdDev})')
        self.mean = mean
        self.stdDev = stdDev

    def value(self):
        return numpy.random.normal(self.mean, self.stdDev)

if __name__ == "__main__":
    print("Don't run this. Run gbIterator instead.")