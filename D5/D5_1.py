# AoC 2019 - Day 5 - Part 1

f = open('input.txt', 'r')
#codes = list(map(int, f.read().split(',')))
codes = f.read().split(',')

i = 0

def get_value(mode, param):
    if mode == 0:
        return int(codes[param])
    else:
        return param


halt = False
while not halt:
    params = 0
    while len(codes[i]) < 5:
        codes[i] = '0' + codes[i]
    inst = codes[i]
    if int(inst[3:]) == 3:
        codes[int(codes[i+1])] = "1"
        i += 2
    elif int(inst[3:]) == 4:
        print(codes[int(codes[i+1])])
        i += 2
    elif int(inst[3:]) == 99:
        halt = True
    elif int(inst[3:]) == 1:
        if int(inst[0]) == 0:
            codes[int(codes[i+3])] = str(get_value(int(inst[2]), int(codes[i+1])) + get_value(int(inst[1]), int(codes[i+2])))
        else:
            codes[i+3] = str(get_value(int(inst[2]), int(codes[i+1])) + get_value(int(inst[1]), int(codes[i+2])))
        i += 4
    elif int(inst[3:]) == 2:
        if int(inst[0]) == 0:
            codes[int(codes[i+3])] = str(get_value(int(inst[2]), int(codes[i+1])) * get_value(int(inst[1]), int(codes[i+2])))
        else:
            codes[i+3] = str(get_value(int(inst[2]), int(codes[i+1])) * get_value(int(inst[1]), int(codes[i+2])))
        i += 4

