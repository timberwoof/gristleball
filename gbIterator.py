"""Gristleball Iterator"""

# *** this needs to import your specific model class
from example import model
from gbResult import result

def main():
    print("main")
    theModel = model() # parameters are set up in user's __init__
    i = 0
    limit = 100
    while i < limit:
        oneResult = theModel.calculate()
        theModel.result.put(oneResult)
        i = i + 1

    theModel.result.plot()

if __name__ == "__main__":
    main()