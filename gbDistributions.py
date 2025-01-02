import random

class gbLinear:
    def __init__(self, xmin=0, xmax=1, ymax=1):
        print(f'initializing gbLinear(xmin={xmin}, max={xmax}, ymax={ymax})')
        self.xmin = xmin
        self.xmax = xmax
        self.ymax = ymax

    def value(self):
        return random.uniform(self.xmin, self.xmax) * self.ymax

class gbTriangular:
    def __init__(self, low=0, mode=0.5, high=1, ymax=1):
        print(f'initializing gbLinear(low={low}, mode={mode}, high={high}, ymax={ymax})')
        self.low = low
        self.mode = mode
        self.high = high
        self.ymax = ymax

    def value(self):
        return random.triangular(self.low, self.high, self.mode) * self.ymax
