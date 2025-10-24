from math import ceil
for t in range(int(input())):
    n = int(input())
    a = [abs(int(i)) for i in input().split()]
    a1 = a[0]

    medianPos = ceil(n/2) - 1
    movable = 0
    for i in a:
        if i > a1: movable += 1 

    print('YES' if movable >= medianPos else 'NO')