"""
clearview.py: example of how to use Gristleball with more distributions.
"""

# In gbIterator, edit the line
# from example import model
# to point to your model file, for example
# from clearview import model

# This example is borrowed from
# "Crystal Ball Version 3.0: Forecasting and Risk Analysis for Sporeadsheet Users",
# Decisioneering, Inc, 1993, pages 19-35.

# Import the distributions we will use in the model.
from gbDistributions import uniform
from gbDistributions import custom
from gbDistributions import triangular
from gbDistributions import binomial
from gbDistributions import normal
from gbDistributions import min

# Required import.
from gbResult import result

class model:
    def __init__(self):
        """Define the inputs to the model we will calculate."""
        # This model represents calculattions to see whether
        # a hypothetical drug company's investment in a new drug
        # will prove profitable.

        # run the simulation this number of times
        self.iterations = 10000

        # Assumptions
        # Costs ($M)
        self.development_costs = 10 # C4
        self.test_costs = uniform(3, 5) # C5
        self.marketing_costs = triangular(12, 16, 18) # C6

        # Drug Test Results
        self.patientsCured = binomial(0.25, 100) # C10
        # A clinical trial of 100 patients, 25% of whom are cured.

        # Market Study
        self.personsWithNearsightedness = 40 # (millions) C14
        self.growthRate = custom([[0.00, 0.05, 0.75], [-0.15, -0.05, 0.25]]) # C15
        # 75% chance that we will see a 5% to 7.5% increase in number of nearsighted people
        # 25% chance that we get a competitor and we get a 5% to 15% drop in number of nearsighted people

        # market penetration
        self.marketPenetration = min(normal(0.08, 0.02), 0.05) #C19
        # Expect 8% market penetration ith a standard deviation of 2%, but at least 5%.
        self.profitPerCustomer = 12 #C20 ($)

        # Forecasts
        self.grossProfit = result("Gross Profit If Approved", "Gross Profit ($M)") # C21
        self.netProfit = result("Net Profit", "Net Profit ($M)") # C23

        self.results = [self.grossProfit, self.netProfit]

    def calculate(self):
        """Calculate the mathematical model for one set of inputs"""

        # Costs
        testCosts = self.test_costs.value() # C5

        # Drug Test
        patientsCured = self.patientsCured.value() # C10
        approved = patientsCured > 20 # C11

        # Market
        personsWithNearsightednessAfter1Year = self.personsWithNearsightedness * (1 + self.growthRate.value()) # C16

        # Gross and Net Profit
        if approved:
            grossProfit = personsWithNearsightednessAfter1Year * self.marketPenetration.value() * self.profitPerCustomer  # C21
            self.grossProfit.put(grossProfit)  # C21
            marketingCosts = self.marketing_costs.value()
        else:
            grossProfit = 0
            # We don't have to call put for profit in this case.
            marketingCosts = 0

        netProfit = grossProfit - (self.development_costs + testCosts + marketingCosts)
        self.netProfit.put(netProfit) #C23

if __name__ == "__main__":
    print("Don't run this. Run python3 monte clearview instead.")