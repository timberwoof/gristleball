"""
test_min.py: test the minimum function.
"""

from gbDistributions import normal
from gbDistributions import min

# Required import.
from gbResult import result

class model:
    def __init__(self):
        self.iterations = 10000
        self.normal = min(normal(10,3),7)
        self.result = result("normal Distribution with Minimum", "normal Distribution with Minimum", 100)
        self.results = [self.result]

    def calculate(self):
        self.result.put(self.normal.value())

if __name__ == "__main__":
    print("Don't run this. Run python3 monte test_normal instead.")