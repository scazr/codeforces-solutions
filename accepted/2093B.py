for t in range(int(input())):
    n = input()

    lastNonZeroIndex = -1
    for i in range(len(n) - 1, -1, -1):
        if n[i] != '0': lastNonZeroIndex = i; break

    removedDigits = len(n) - (lastNonZeroIndex + 1)

    for i in range(lastNonZeroIndex):
        if n[i] != '0': removedDigits += 1

    print(removedDigits)

