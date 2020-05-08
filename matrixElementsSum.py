def matrixElementsSum(matrix):
    t = list(zip(*matrix))
    sum = 0
    for i in range(len(t)):
        for j in range(len(t[0])):
            sum = sum + t[i][j]
            if t[i][j] == 0:
                break
    return sum
