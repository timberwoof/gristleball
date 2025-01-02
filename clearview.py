"""
clearview.py: example of how to use Gristleball with more distributions.
"""

# In gbIterator, edit the line
# from example import model
# to point to y our model file, for example
# from clesrview import model

# We need to import the distributions we will use in the model.
# In this example we will use one linear distribution and one triangular.
# If your model uses more distributions, add them here.
from gbDistributions import linear
from gbDistributions import custom
from gbDistributions import triangular
from gbDistributions import binomial
from gbDistributions import normal

# Required import.
from gbResult import result

class model:
    def __init__(self):
        """Define the inputs to the model we will calculate."""

        # Required Value:
        # run the simulation this number of times
        self.iterations = 10000

        # Costs ($M)
        self.development_costs = 10 # C4
        self.test_costs = linear(3, 5) # C5
        self.marketing_costs = 16 # C6

        # Drug Test
        self.patientsCured = binomial(0.25, 100) # C10
        # approved = patientsCured > 20 # C11

        # Market Study
        self.personsWithNearsightedness = 40 # C14
        self.growthRate = custom(0.2) # C15

        # market penetration
        self.marketPenetration = normal(0.08, 0.02) #C19
        self.profitPerCustomer = 300 #C20 *** made up number

        # Forecasts
        self.grossProfit = result("Gross Profit", "Gross Profit ($M)") # C21
        self.netProfit = result("Net Profit", "Net Profit ($M)") # C23

        self.results = [self.grossProfit, self.netProfit]

    def calculate(self):
        """Calculate the mathematical model for one set of inputs"""

        # Costs
        testCosts = self.test_costs.value()
        totalCosts = self.development_costs + testCosts + self.marketing_costs # C7

        # Drug Test
        patientsCured = self.patientsCured.value() # C8
        approved = patientsCured > 20

        # Market
        personsWithNearsightednessAfter1Year = self.personsWithNearsightedness * self.growthRate.value()
        grossProfit = personsWithNearsightednessAfter1Year * self.marketPenetration.value() * self.profitPerCustomer # C21

        netProfit = 0
        if approved:
            netPreofit = grossProfit - totalCosts
        else:
            netProfit = 0 - self.development_costs - testCosts

        self.grossProfit.put(grossProfit)
        self.netProfit.put(netProfit)

if __name__ == "__main__":
    print("Don't run this. Run gbIterator instead.")