# AoC 2019 - Day 1 - Part 1

f = open('input.txt', 'r')

sum = 0

for l in f:
    sum += int(int(l)/3)-2
print(sum)