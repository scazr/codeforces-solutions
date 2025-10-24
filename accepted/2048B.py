for t in range(int(input())):
    n, k = map(int, input().split())

    ans = [0 for i in range(n)]
    j = 1
    for i in range(k-1, len(ans), k):
        ans[i] = j
        j += 1
    
    for i in range(len(ans)):
        if ans[i] == 0: 
            ans[i] = j
            j += 1
        
    print(' '.join(map(str, ans)))