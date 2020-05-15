def allLongestStrings(inputArray):
    a = max([len(i) for i in inputArray])
    list = [i for i in inputArray if len(i) == a]
    return list