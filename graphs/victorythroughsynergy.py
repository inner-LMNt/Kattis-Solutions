edges = int(input())

adjacency_matrix = [[] for _ in range(10)]

for _ in range(edges):
    numbers = input().split()
    a = int(numbers[0])
    b = int(numbers[1])

    adjacency_matrix[a].append(b)
    adjacency_matrix[b].append(a)

players = []
for _ in range(10):
    player = input().split()
    country = player[1]
    league = player[2]
    team = player[3]

    players.append((country, league, team))

# Precalculate player synergies
power_matrix = [[0 for _ in range(10)] for _ in range(10)]
for i in range(10):
    for j in range(10):
        if i == j:
            continue
        if players[i][0] == players[j][0]: # matching country
            power_matrix[i][j] += 1
        if players[i][1] == players[j][1]: # matching league
            power_matrix[i][j] += 1
        if players[i][2] == players[j][2]: # matching team
            power_matrix[i][j] += 2

# Iterate through all permutations of players to find if there is synergy
from itertools import permutations

player_nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
perms = list(permutations(player_nums))

for perm in perms:
    valid = True
    for i in range(10):
        degree = len(adjacency_matrix[i])
        power = 0
        for neighbor in adjacency_matrix[i]:
            power += power_matrix[perm[i]][perm[neighbor]]

        if power < degree:
            valid = False
    if valid:
        print("yes")
        exit()

print("no")
