from collections import Counter

for t in range(int(input())):
    n = int(input())
    s = input()
    freqList = Counter(s).most_common()
    si = freqList[0][0]
    sj = freqList[-1][0]

    print(s.replace(sj, si, 1))