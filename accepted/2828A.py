for t in range(int(input())):
    n, a, b = map(int, input().split())
    s = input()

    alice = [0, 0]
    queen = [a, b]
    ref = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}

    found = False
    for i in range(21):
        for ch in s:
            alice[0], alice[1] = alice[0] + ref[ch][0], alice[1] + ref[ch][1]
            if alice == queen:
                found = True
                break
        if found: break
    print('YES' if found else 'NO')

