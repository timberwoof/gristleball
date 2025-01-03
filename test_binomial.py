"""
test_binomial.py: test the Custom distribution.
"""

from gbDistributions import binomial

# Required import.
from gbResult import result

class model:
    def __init__(self):
        self.iterations = 10000
        self.binomial = binomial(.5,100)
        self.result = result("binomial Distribution", "binomial Distribution", 100)
        self.results = [self.result]

    def calculate(self):
        self.result.put(self.binomial.value())

if __name__ == "__main__":
    print("Don't run this. Run python3 monte test_binomial instead.")