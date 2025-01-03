"""
testtriangular.py: test the Custom distribution.
"""

from gbDistributions import triangular

# Required import.
from gbResult import result

class model:
    def __init__(self):
        self.iterations = 10000
        self.triangular = triangular(0,1, 4)
        self.result = result("triangular Distribution", "triangular Distribution", 100)
        self.results = [self.result]

    def calculate(self):
        self.result.put(self.triangular.value())

if __name__ == "__main__":
    print("Don't run this. Run gbIterator instead.")