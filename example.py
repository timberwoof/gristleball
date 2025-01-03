"""
example.py: simple cookbook example of how to use Gristleball.
This is a very simple model of monthly income from an apartment block.
"""

# Copy this file to a new python file with a name like myModel.py .
# Add the distributions you need to use and instantiate them in __init__.
# Write your Calculate function the way you want it.
# In gbIterator, edit the line
# from example import model
# to point to your model file, for example
# from myModel import model

# We need to import the distributions we will use in the model.
# In this example we will use one linear distribution and one triangular.
# If your model uses more distributions, add them here.
from gbDistributions import uniform
from gbDistributions import triangular

# Required import.
from gbResult import result

class model:
    def __init__(self):
        """Define the inputs to the model we will calculate."""

        # Required Value:
        # run the simulation this number of times
        self.iterations = 1000

        # The reso of this class is your cusotm code.
        # apartment block has 10 units
        self.units = 10

        # occupancy could be anywhere between 80% and 100%
        # with an equal likelihood of any level of occupancy.
        self.occupancy = uniform(0.8, 1.0)

        # We try to rent units at a fair rate, $200/month
        # but sometimes we give breaks to people
        # and sometimes we charge more.
        self.rentalRate = triangular(1800, 2200, 2400)

        # Here we set up where the calculations end up.
        self.result = result("Rental Income", "Monthly Income ($)", 20)

        self.results = [self.result]

    def calculate(self):
        """Calculate the mathematical model for one set of inputs"""

        # This model is pretty simple. We multiply the two values
        # and put them into the result accumulator.
        self.result.put(self.occupancy.value() * self.rentalRate.value() * self.units)

if __name__ == "__main__":
    print("Don't run this. Run python3 monte example instead.")