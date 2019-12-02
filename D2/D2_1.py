# AoC 2019 - Day 2 - Part 1

f = open('input.txt', 'r')
codes = list(map(int, f.read().split(',')))

codes[1] = 12
codes[2] = 2

i = 0
for code in codes:
    if i % 4 == 0:
        if code == 1:
            codes[codes[i + 3]] = codes[codes[i + 1]] + codes[codes[i + 2]]
        elif code == 2:
            codes[codes[i + 3]] = codes[codes[i + 1]] * codes[codes[i + 2]]
        elif code == 99:
            break
    i += 1

print(codes[0])
