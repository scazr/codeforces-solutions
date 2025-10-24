for t in range(int(input())):
    n, k = map(int, input().split())
    a = [int(i) for i in input().split()]

    progress = 0
    concluded = 0
    resting = False
    for i in a:
        if resting:
            resting = False
            continue

        if i == 0: progress += 1
        else: progress = 0

        if progress == k:
            progress = 0
            concluded += 1
            resting = True
        
    print(concluded)