"""
test_max.py: test the maximum function.
"""

from gbDistributions import normal
from gbDistributions import max

# Required import.
from gbResult import result

class model:
    def __init__(self):
        self.iterations = 10000
        self.normal = max(normal(10,3),13)
        self.result = result("normal Distribution with Maximum", "normal Distribution with Maximum", 100)
        self.results = [self.result]

    def calculate(self):
        self.result.put(self.normal.value())

if __name__ == "__main__":
    print("Don't run this. Run python3 monte test_normal instead.")