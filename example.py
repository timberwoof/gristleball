"""
example.py: simple cookbook example of how to use Grstleball.
This example models the monthly income from an apartment block.
"""

# We need to import the distributions we will use in the model.
# In this example we will use one linear distribution and one triangular.
from gbDistributions import gbLinear
from gbDistributions import gbTriangular
from gbResult import result

class example:
    def __init__(self):
        """Define the inputs to the model we will calculate."""

        # occupancy could be anywhere between 80% and 100%
        # with an equal likelihood of any level of occupancy.
        self.occupancy = gbLinear(0.8, 1.0, 1.0)

        # We try to rent units at a fair rate, $200/month
        # but sometimes we give breaks to people
        # and sometimes we charge more.
        self.rentalRate = gbTriangular(1800, 2200, 2400)

        # Here we set up where the calculations end up
        self.result = result("Rental income", "Income", "#", 0, 100000, 100)

    def calculate(self):
        """Calculate the mathematical model for one set of inputs"""

        # This model is pretty simple. We multiply the two values
        # and give them back to the iterator.
        return self.occupancy * self.rentalRate