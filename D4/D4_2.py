# AoC 2019 - Day 4 - Part 2

f = open('input.txt', 'r')

code_range = list(map(int, f.readline().split('-')))

sum = 0

for i in range(code_range[0], code_range[1]):
    code = str(i)
    doubles = 0
    wrong = False
    before_previous_digit = -1
    previous_digit = -1
    j = 0
    for digit in code:
        if int(digit) >= previous_digit:
            if int(digit) == previous_digit:
                if (j+1 == len(code)):
                    if int(digit) != before_previous_digit:
                        doubles = 1
                else:
                    if int(digit) != before_previous_digit and int(code[j+1]) != int(digit):
                        doubles = 1
        else:
            wrong = True
        before_previous_digit = previous_digit
        previous_digit = int(digit)
        j += 1
    if doubles == 1 and wrong == False:
        sum += 1
print(sum)