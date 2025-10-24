from collections import Counter

def main():
    for t in range(int(input())):
        n, k = map(int, input().split())
        s = input()

        if len(Counter(s)) > 1 and k > 0: print('YES')
        elif s < s[::-1]: print('YES')
        else: print('NO')

main()
