from math import floor, ceil

def main():
    for i in range(int(input())):
        n = int(input())
        s = input()
        c = s.count('-')

        print(floor(c/2)*ceil(c/2) * (n-c))

main()