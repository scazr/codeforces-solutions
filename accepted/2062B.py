for t in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]

    for i in range(n):
        if max(i, n-i-1)*2 >= a[i]: print('NO'); break
    else: print('YES')