# AoC 2019 - Day 6 - Part 2

f = open('input.txt', 'r')
orbits = f.read().split('\n')
planets = {'COM': 0}


def get_path(planet, path):
    path.append(planets[planet])
    if planet == "COM":
        return path
    return get_path(planets[planet], path)


for orbit in orbits:
    planet = orbit.split(')')
    planets[planet[1]] = planet[0]

san = get_path('SAN', [])
you = get_path('YOU', [])

for i in range(0, len(san)):
    for j in range(0, len(you)):
        if san[i] == you[j] and san[i - 1] != you[j - 1]:
            sum = i + j
            print(sum)
            break
