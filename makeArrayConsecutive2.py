def makeArrayConsecutive2(statues):
    return len(set(range(min(statues),max(statues))) - set(statues))
