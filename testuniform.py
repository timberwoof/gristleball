"""
testuniform.py: test the Custom distribution.
"""

from gbDistributions import uniform

# Required import.
from gbResult import result

class model:
    def __init__(self):
        self.iterations = 10000
        self.uniform = uniform(2,5)
        self.result = result("Uniform Distribution", "Uniform Distribution", 100)
        self.results = [self.result]

    def calculate(self):
        self.result.put(self.uniform.value())

if __name__ == "__main__":
    print("Don't run this. Run gbIterator instead.")