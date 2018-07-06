planet_list = ["Mercury", "Mars"]
planet_list.append("Jupiter")
planet_list.append("Saturn")
print(planet_list)
planet_list.extend(['Uranus', 'Neptune'])
print(planet_list)
planet_list.insert(2, 'Earth')
planet_list.insert(3, 'Venus')
print(planet_list)
planet_list.append('Pluto')
print(planet_list)
rocky_planets = planet_list[4:]
print(rocky_planets)
print(len(planet_list))
del planet_list[8]
print(planet_list)
