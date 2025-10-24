from math import ceil
for t in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]

    if n == 1: print('NO')
    else: print('YES' if sum(a) >= n + a.count(1) else 'NO')