vowels = 'aeiou'
for t in range(int(input())):
    n = int(input())
    if n <= 5: print(vowels[0:n])
    else:
        div = n // 5
        rem = n % 5

        print(vowels[0] * (div + (1 if rem >= 1 else 0)) + vowels[1] * (div + (1 if rem >= 2 else 0)) + vowels[2] * (div + ((1 if rem >= 3 else 0) ))+ vowels[3] * (div + (1 if rem >= 4 else 0)) + vowels[4] * (div + (1 if rem >= 5 else 0)))
