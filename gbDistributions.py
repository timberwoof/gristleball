"""Random distributions for Gristleball"""
# Each of these provides one distribution types to feed your model.
# You can instantiate as many of these as you need to.
# Sure, you can add new distribution types to his file.
# Please submit them to the GitHub project along with a test class.
#
# Every distribution class must have the methods
# __init__ that takes the parameters for the distribution
# value() that returns one value
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

class normal:
    def __init__(self, mean, stdDev):
        print(f'initializing normal(mean={mean}, stdDev={stdDev})')
        self.mean = mean
        self.stdDev = stdDev

    def value(self):
        return numpy.random.normal(self.mean, self.stdDev)

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
    #
    # The data structure looks like [[0.0, 0.05, 0.75], [-0.15, -0.05, 0.25]]
    # The first two parameters are the limits for this range.
    # The third parameter Prob is the probability that the value will be in this range.
    # We don't care what order the blocks are in.
    #
    # Crystal Ball 3.0 allowed you to specify the Y values for the start and end of each range.
    # This does not. If you need that, please write it up and submit it as optional parameters to __init__.

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

        # Normalize each block's probability
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

class min():
    """Limit a distribution's minimum value"""
    # define your function as min calling the distribution:
    # self.a_distribution = min(normal(8, 2), 4)  # C19
    # and call it as usual:
    # self.a_distribution.value()
    # The iteration limit of 10 is arbitrary.

    def __init__(self, distribution, mininmum=0):
        self.distribution = distribution
        self.mininmum = mininmum

    def value(self):
        value = self.distribution.value()
        iterations = 0
        while value < self.mininmum and iterations < 10:
            value = self.distribution.value()
            iterations = iterations + 1
        return value

class max():
    """Limit a distribution's maximum value"""
    # define your function as max calling the distribution:
    # self.a_distribution = max(normal(8, 2), 12)  # C19
    # and call it as usual:
    # self.a_distribution.value()
    # The iteration limit of 10 is arbitrary.

    def __init__(self, distribution, maximum=0):
        self.distribution = distribution
        self.maximum = maximum

    def value(self):
        value = self.distribution.value()
        iterations = 0
        while value > self.maximum and iterations < 10:
            value = self.distribution.value()
            iterations = iterations + 1
        return value

if __name__ == "__main__":
    print("Don't run this. Run python3 monte instead.")