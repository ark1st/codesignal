def isLucky(n):
    a = [int(i) for i in str(n)]
    return True if  sum(a[:len(a)//2]) == sum(a[len(a)//2:]) else False
