# AoC 2019 - Day 3 - Part 2
# I have not found a more efficient way to solve this. It just takes let's say a lifetime :D

f = open('input.txt', 'r')

wire_one = f.readline().split(',')
wire_two = f.readline().split(',')
directions_x = {'U': 0, 'D': 0, 'L': -1, 'R': 1}
directions_y = {'U': 1, 'D': -1, 'L': 0, 'R': 0}

def wire_to_points(wire):
    points = [[0, 0, 0]]
    i = 0
    for command in wire:
        direction = command[0]
        length = int(command[1:])
        for _ in range(length):
            points.append([points[i][0] + directions_x[direction], points[i][1] + directions_y[direction], i+1])
            i += 1
    return points


points_one = wire_to_points(wire_one)
points_two = wire_to_points(wire_two)

steps = []

for a in points_one:
    for b in points_two:
        if a[0] == b[0] and a[1] == b[1]:
            steps.append(a[2] + b[2])
            print(a[2] + b[2])

steps.sort()
print(steps[1])