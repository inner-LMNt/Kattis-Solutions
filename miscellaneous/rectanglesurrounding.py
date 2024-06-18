import sys

data = [] # data extraction
for line in sys.stdin:
    data.append(line.split())

i = 0
while i < len(data):
    times = int(data[i][0]) # number of rectangles
    if times == 0: # end of input
        break

    coordinates = []
    max_x = 0 # max x and y coordinates
    max_y = 0 # to help generate a somewhat minimum visited array

    for j in range(times):
        coordinate = [(data[i+j+1][0], data[i+j+1][1]), (data[i+j+1][2], data[i+j+1][3])]
        max_x = max(max_x, int(data[i+j+1][0]), int(data[i+j+1][2]))
        max_y = max(max_y, int(data[i+j+1][1]), int(data[i+j+1][3]))
        coordinates.append(coordinate)

    result = 0
    visited = [[0 for y in range(max_y)] for x in range(max_x)]

    # simply mark each rectangle in the visited array
    for j in range(times):
        for k in range(int(coordinates[j][0][0]), int(coordinates[j][1][0])):
            for l in range(int(coordinates[j][0][1]), int(coordinates[j][1][1])):
                if visited[k][l] == 0:
                    visited[k][l] = 1
                    result += 1

    print(result)

    i += times + 1 # next batch of input