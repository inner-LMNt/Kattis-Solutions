test_cases = int(input())

for _ in range(test_cases):
    routers, houses = map(int, input().split())
    addresses = []
    for i in range(houses):
        addresses.append(int(input()))
    addresses.sort()

    # Worst case is put just one router in the middle, range is distance between first and last house
    upper_distance = addresses[-1] - addresses[0]
    lower_distance = 0

    # Binary search for the optimal max diameter of a router
    while lower_distance <= upper_distance:
        distance = (lower_distance + upper_distance) // 2

        index = 0
        routers_needed = 0
        while index < len(addresses):
            routers_needed += 1
            # Left end of router range starts at current house
            next_distance = addresses[index] + distance # right end of router range
            index += 1 # current house is always in range

            # Skip through houses that are within router range
            while index < len(addresses) and addresses[index] <= next_distance:
                index += 1

        if routers_needed <= routers: # if equal, we can still try to do better
            upper_distance = distance - 1
        else:
            lower_distance = distance + 1

    print(lower_distance / 2) # divide by 2 since distance to edge is half of diameter