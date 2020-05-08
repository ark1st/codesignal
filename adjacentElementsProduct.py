def adjacentElementsProduct(inputArray):
    a = inputArray[0]*inputArray[1]
    for i in range(len(inputArray)-1):
        if a < inputArray[i]*inputArray[i+1]:
            a = inputArray[i]*inputArray[i+1]
    return a
