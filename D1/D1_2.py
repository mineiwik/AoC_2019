f = open('input.txt', 'r')
sum = 0

def fuel_adder(amount):
    partial = int(amount/3)-2
    if partial < 1:
        return 0
    return partial + fuel_adder(partial)

for l in f:
    sum += fuel_adder(int(l))

print(sum)