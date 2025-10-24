for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    aSort = sorted(a)

    aDeranged = []
    idx = 0
    for i in range(n):
        if idx > n: break
        if a[i] != aSort[i]: 
            aDeranged.append(str(a[i]))
    
    if aDeranged:
        print('YES')
        print(len(aDeranged))
        print(' '.join(aDeranged))
    else:
        print('NO')
    

