"""
test_custom.py: test the Custom distribution.
"""

from gbDistributions import custom

# Required import.
from gbResult import result

class model:
    def __init__(self):
        self.iterations = 10000
        self.custom = custom([[-5, -2, 1], [0, 1, 5], [2, 3, 1]])
        self.result = result("Custom Distribution", "X Value", 100)
        self.results = [self.result]

    def calculate(self):
        self.result.put(self.custom.value())

if __name__ == "__main__":
    print("Don't run this. Run gbIterator instead.")