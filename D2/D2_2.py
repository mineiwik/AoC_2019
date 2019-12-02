# AoC 2019 - Day 2 - Part 2

f = open('input.txt', 'r')
codes = list(map(int, f.read().split(',')))

for a in range(0, 100):
    for b in range(0, 100):
        copy_codes = codes.copy()
        copy_codes[1] = a
        copy_codes[2] = b
        i = 0
        for code in copy_codes:
            if i % 4 == 0:
                if code == 1:
                    copy_codes[copy_codes[i + 3]] = copy_codes[copy_codes[i + 1]] + copy_codes[copy_codes[i + 2]]
                elif code == 2:
                    copy_codes[copy_codes[i + 3]] = copy_codes[copy_codes[i + 1]] * copy_codes[copy_codes[i + 2]]
                elif code == 99:
                    break
            i += 1
        if copy_codes[0] == 19690720:
            result = 100 * copy_codes[1] + copy_codes[2]
            print(result)
            break
