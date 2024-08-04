test_cases = int(input())

for _ in range(test_cases):
    climbs = int(input())

    if climbs == 1: # degenerate case
        temp = input()
        print("IMPOSSIBLE")
        continue

    distances = list(map(int, input().split()))

    if sum(distances) % 2 == 1: # odd distances cannot return to start
        print("IMPOSSIBLE")
        continue

    # Worst case is half the total distance
    dim = sum(distances) // 2
    dim += 1

    # max_heights[x][y] is the maximum height needed to be at height x with y climbs
    max_heights = [[dim for _ in range(climbs)] for _ in range(dim)]

    # direction[x][y] is the direction to taken to reach max_heights[x][y]
    direction = [[None for _ in range(climbs)] for _ in range(dim)]

    # First climb
    max_heights[distances[0]][0] = distances[0]
    direction[distances[0]][0] = "U"

    for i in range(1, climbs):
        for j in range(dim):
            if max_heights[j][i-1] == dim:
                continue
            
            up = j + distances[i]
            if up < dim: # go up, has the potential to increase the max
                potential_max = max(max_heights[j][i-1], up)
                if potential_max < max_heights[up][i]: # if most optimal so far, store it
                    max_heights[up][i] = potential_max
                    direction[up][i] = "U"

            down = j - distances[i]
            if down >= 0: # go down
                if max_heights[j][i-1] < max_heights[down][i]: # if coming from a more optimal path
                    max_heights[down][i] = max_heights[j][i-1]
                    direction[down][i] = "D"

    # Did not reach the bottom at the end
    if max_heights[0][climbs-1] == dim:
        print("IMPOSSIBLE")
        continue

    # Backtrack to find the path
    path = ""
    current_height = 0
    for i in reversed(range(climbs)):
        if direction[current_height][i] == "U":
            path += "U"
            current_height -= distances[i]
        else:
            path += "D"
            current_height += distances[i]

    print(''.join(reversed(path)))
