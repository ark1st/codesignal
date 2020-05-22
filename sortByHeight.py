def sortByHeight(a):
    trees = [i for i in range(len(a)) if a[i] == -1]
    sorted_arr = sorted([i for i in a if i >= 0])
    for i in trees:
        sorted_arr.insert(i, -1)
    return sorted_arr
