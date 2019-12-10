# AoC 2019 - Day 8 - Part 1

import math

f = open('input.txt', 'r')
digits = f.read()

layer_amount = 25*6
counter = 0
layers = []

while counter < len(digits):
    layers.append(digits[counter:(counter+layer_amount)])
    counter += layer_amount

previous_zeros = math.inf
lowest_layer = 0
for i in range(0, len(layers)):
    current_zeros = 0
    for digit in layers[i]:
        if int(digit) == 0:
            current_zeros += 1
    if current_zeros < previous_zeros:
        previous_zeros = current_zeros
        lowest_layer = i

sum_1 = 0
sum_2 = 0
for digit in layers[lowest_layer]:
    current_digit = int(digit)
    if current_digit == 1:
        sum_1 += 1
    elif current_digit == 2:
        sum_2 += 1

print(sum_1*sum_2)
