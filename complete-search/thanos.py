import sys

# Data extraction
data = []
for line in sys.stdin:
    data.append(line.split())

for line in data:
    if len(line) == 1: # Skip `T`, not needed here
        continue
    
    population = int(line[0])
    growth = int(line[1])
    maximum = int(line[2])

    result = 0

    # Calculate the time until the planet becomes unsustainable.
    while population <= maximum:
        population *= growth
        result += 1

    print(result)