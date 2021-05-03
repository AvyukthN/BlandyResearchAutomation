import pandas as pd
import numpy as np
from numpy.lib.scimath import logn
from math import e
from matplotlib import pyplot as plt
  
df = pd.DataFrame(pd.read_excel("C:/Users/avyuk/Desktop/Learn/Coding/Automation/BlandyAutomation/Blandy_Data.xlsx"))

datahash = {}
for col in df:
    datahash.update({col: list(df[col])})

PlotID = datahash['PlotID / Year Plowed']
Quantity = datahash['Quantity']

PlotIDhash = {}

count = 0
for i in range(len(PlotID)):
    if (PlotID[i] not in PlotIDhash) and (isinstance(PlotID[i], str)):
        PlotIDhash.update({PlotID[i]: count})
        count += 1
 
def index_finder(index):
    for somePlotID in PlotIDhash:
        if PlotIDhash[somePlotID] == index:
            return somePlotID

tempQuantArr = []
count = 0

for i in range(len(Quantity)):
    if (isinstance(Quantity[i], float) and not(np.isnan(Quantity[i]))):
        tempQuantArr.append(Quantity[i])
    if np.isnan(Quantity[i]) or (i == (len(Quantity) - 1)):
        toUpdate = index_finder(count)
        PlotIDhash.update({toUpdate: tempQuantArr})
        tempQuantArr = []
        count += 1

def HPrime(arr):
    bi = []
    lnOfbi = []
    bi_x_lnOfbi = []
    speciesTotal = sum(arr, 0)

    for i in range(len(arr)):
        bi.append(arr[i] / speciesTotal)
    for i in range(len(bi)):
        lnOfbi.append(logn(e, bi[i]))
    for i in range(len(bi)):
        bi_x_lnOfbi.append(bi[i] * lnOfbi[i])

    return [sum(bi_x_lnOfbi), speciesTotal/len(arr), len(arr)]

def JPrime(Hprime, EvenNum, length):
    arr = []
    for i in range(length):
        arr.append(EvenNum)
    
    newHPrime = HPrime(arr)[0]

    return Hprime/newHPrime

if __name__ == '__main__':
    PlotIDs = []
    HPrimes = []
    JPrimes = []
    tempHPrimes = []
    tempJPrimes = []
    HPrimeHash = {}
    JPrimeHash = {}

    for key in PlotIDhash:
        HPrimeReturn = HPrime(PlotIDhash[key])

        PlotID = key
        HPrimeVal = HPrimeReturn[0]
        JPrimeVal = JPrime(HPrimeReturn[0], HPrimeReturn[1], HPrimeReturn[2])

        PlotIDs.append(PlotID)
        HPrimes.append(HPrimeVal)
        JPrimes.append(JPrimeVal)
        tempHPrimes.append(HPrimeVal)
        tempJPrimes.append(JPrimeVal)

        HPrimeHash.update({HPrimeVal: key})
        JPrimeHash.update({JPrimeVal: key})

    tempHPrimes.sort(reverse=True)
    tempJPrimes.sort(reverse=True)

    for i in range(len(tempHPrimes)):
        tempHPrimes[i] = HPrimeHash[tempHPrimes[i]]
        tempJPrimes[i] = JPrimeHash[tempJPrimes[i]]

    OutputTable = {'PlotID': pd.Series(PlotIDs), 
                   'H\' Value': pd.Series(HPrimes), 
                   'J\' Value': pd.Series(JPrimes),
                   ' H\' Ranking': pd.Series(tempHPrimes),
                   ' J\' Ranking': pd.Series(tempJPrimes)}

    OutputTable = pd.DataFrame(OutputTable)

    index = OutputTable.index
    index.name = "Plot Number"
    OutputTable.index += 1

    print("\n")
    print(df)
    print("\n")
    print(OutputTable)
    print("\n")