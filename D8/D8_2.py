# AoC 2019 - Day 8 - Part 2

import math

f = open('input.txt', 'r')
digits = f.read()

layer_amount = 25*6
counter = 0
layers = []

while counter < len(digits):
    layers.append(digits[counter:(counter+layer_amount)])
    counter += layer_amount

result = [2] * layer_amount

for digit in range(0, layer_amount):
    for layer in range(0, len(layers)):
        if result[digit] == 2:
            if int(layers[layer][digit]) == 0:
                result[digit] = " "
            elif int(layers[layer][digit]) == 1:
                result[digit] = "#"
            else:
                result[digit] = 2
image = [""]*6
for j in range(0,6):
    for i in range(0,25):
        image[j] += str(result[i+25*j])
    print(image[j])