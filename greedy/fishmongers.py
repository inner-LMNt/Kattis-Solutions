n, m = map(int, input().split())
fish_weights = list(map(int, input().split()))

fish_weights.sort()

fishmongers = []
for i in range(m):
    num, price = map(int, input().split())
    fishmongers.append((num, price))

# sort by max offer price per pound
fishmongers.sort(key=lambda x: x[1])

result = 0
m -= 1

while n > 0:
    # move to the next fishmonger once we run out
    if fishmongers[m][0] == 0:
        m -= 1
    
    # if no fishmongers left, exit
    if m < 0:
        break

    # at this point, we have chosen the most lucrative seller
    result += fishmongers[m][1] * fish_weights[n - 1]
    fishmongers[m] = (fishmongers[m][0] - 1, fishmongers[m][1])
    n -= 1

print(result)
