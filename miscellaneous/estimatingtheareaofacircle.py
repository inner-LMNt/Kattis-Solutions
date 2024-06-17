import sys
import math

# Data extraction
data = []
for line in sys.stdin:
    data.append(line.split())
    
for line in data:
    r = float(line[0]) # true radius
    m = int(line[1]) # total number of marked points
    c = int(line[2]) # number of marked points in circle

    if r == 0 and m == 0 and c == 0:
        break

    square_area = (r * 2) ** 2
    circle_area = math.pi * r ** 2
    estimate_area = (c / m) * square_area

    print(circle_area, estimate_area)