# AoC 2019 - Day 4 - Part 1

f = open('input.txt', 'r')

code_range = list(map(int, f.readline().split('-')))

sum = 0

for i in range(code_range[0], code_range[1]):
    code = str(i)
    doubles = 0
    wrong = False
    before_previous_digit = -1
    previous_digit = -1
    for digit in code:
        if int(digit) >= previous_digit:
            if int(digit) == previous_digit:
                doubles = 1
        else:
            wrong = True
        previous_digit = int(digit)
    if doubles == 1 and wrong == False:
        sum += 1
print(sum)