letters, weight = map(int, input().split())

if letters * 26 < weight or weight < letters: # too few or too many letters provided
    print("impossible")
    exit()

result = ""

# Greedily fill in with the highest weighted letters possible
while letters < weight:
    # Required to have remaining weight be at least remaining letter amount
    if weight - 26 >= letters - 1: # if we can choose 'z'
        result += 'z'
        letters -= 1
        weight -= 26
    else: # choose letter that will allow us to pad the rest with 'a'
        excess = weight - letters + 1
        result += chr(ord('a') + excess - 1)
        letters -= 1
        weight -= excess
        break

while letters > 0:
    result += 'a'
    letters -= 1

print(result)
