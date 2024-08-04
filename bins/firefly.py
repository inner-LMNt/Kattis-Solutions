from collections import defaultdict

length, height = map(int, input().split())

# Dictionaries to store number of tips at each level
floor_thingies = defaultdict(lambda: 0) # stalagmites
ceiling_thingies = defaultdict(lambda: 0) # stalactites

for i in range(length):
    size = int(input())
    
    if i % 2 == 0: # if floor
        tip = size - 1
        floor_thingies[tip] += 1
    else:
        tip = height - size
        ceiling_thingies[tip] += 1

# Number of obstacles at each level
levels = [0 for _ in range(height)]

# Sweep from bottom to top, adding stalagmites
obstacles = 0
for i in range(height):
    if i in ceiling_thingies:
        obstacles += ceiling_thingies[i]
    levels[i] += obstacles

# Sweep from top to bottom, adding stalactites
obstacles = 0
for i in range(height - 1, -1, -1):
    if i in floor_thingies:
        obstacles += floor_thingies[i]
    levels[i] += obstacles

min_level = min(levels)
min_level_count = levels.count(min_level)

print(min_level, min_level_count)
