def ljutnja_greedy():
    candies, n = map(int, input().split())

    children = []
    for i in range(n):
        children.append(int(input()))

    children.sort(reverse=True) # most greedy children first

    index = 0
    height = children[0]

    # Because anger levels are squared, we want to distribute as evenly as possible
    # Think of distributing by layer, cutting slices off the top of a pyramid of values
    while candies > 0:
        while index < n and children[index] == height: # find next layer width
            index += 1

        if candies < index: # not enough for full layer
            break

        candies -= index
        height -= 1
        
    for i in range(index): # take slicings into effect
        children[i] = height

    for i in range(candies): # distribute remaining candies
        children[i] -= 1

    sum_of_squares = 0
    for i in range(n):
        sum_of_squares += children[i] * children[i]

    print(sum_of_squares)


def ljutnja_binary_search():
    candies, n = map(int, input().split())

    children = []
    for i in range(n):
        children.append(int(input()))

    children.sort(reverse=True) # most greedy children first

    higher = children[0]
    lower = 0
    candies_distributed = 0
    max_height = 0

    # Binary search for the maximum height remaining after optimal distribution
    while lower < higher:
        middle = (lower + higher) // 2
        candies_distributed = 0
        max_height = children[0] - middle

        for i in range(n): # distribute until each child is at most `max_height`
            if children[i] <= max_height:
                break
            candies_distributed += children[i] - max_height

        if candies_distributed <= candies:
            lower = middle + 1
        else:
            higher = middle

    # Found the max height where minimal candies remaining after distribution
    max_height = children[0] - lower + 1

    # First distribute until `max_height`
    candies_distributed = 0
    for i in range(n):
        if children[i] <= max_height:
            break
        candies_distributed += children[i] - max_height

    candies_left = candies - candies_distributed

    # Calculate anger while distributing remaining candies
    sum_of_squares = 0
    for i in range(n):
        if children[i] >= max_height:
            if candies_left > 0:
                sum_of_squares += (max_height - 1) * (max_height - 1)
                candies_left -= 1
            else:
                sum_of_squares += (max_height) * (max_height)
        else:
            sum_of_squares += children[i] * children[i]

    print(sum_of_squares)


from random import randint

# Either solution works
if randint(0, 1) == 0:
    ljutnja_greedy()
else:
    ljutnja_binary_search()
