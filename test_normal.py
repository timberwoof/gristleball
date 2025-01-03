"""
test_normal.py: test the Custom distribution.
"""

from gbDistributions import normal

# Required import.
from gbResult import result

class model:
    def __init__(self):
        self.iterations = 10000
        self.normal = normal(10,3)
        self.result = result("normal Distribution", "normal Distribution", 100)
        self.results = [self.result]

    def calculate(self):
        self.result.put(self.normal.value())

if __name__ == "__main__":
    print("Don't run this. Run gbIterator instead.")