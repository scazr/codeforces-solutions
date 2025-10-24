import math
for i in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    permDist = [abs(p[_]-1 - _) for _ in range(n)]
    print(math.gcd(*permDist))