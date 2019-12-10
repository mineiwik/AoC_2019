# AoC 2019 - Day 6 - Part 1

f = open('input.txt', 'r')
orbits = f.read().split('\n')
planets = {'COM': 0}
sum = 0

def get_orbits(planet):
    if planet == 'COM':
        return 0
    return 1 + get_orbits(planets.get(planet))

for orbit in orbits:
    planet = orbit.split(')')
    planets[planet[1]] = planet[0]

for orbit in orbits:
    planet = orbit.split(')')
    sum += get_orbits(planet[1])

print(sum)