def careful_ascent_math():
    x_coordinate, y_coordinate = map(int, input().split())
    N = int(input())
    shield_thickness_total = 0
    shield_time_total= 0

    for _ in range(N):
        input_data = input().split()
        lower = int(input_data[0])
        upper = int(input_data[1])
        multiplier = float(input_data[2])
        thickness = upper - lower
        shield_thickness_total += thickness

        # The effective time spent traveling through a shielded region in the x-direction 
        shield_time_total += thickness * multiplier

    # Time spent in shieldless regions is equal to height of the region
    no_shield_region_height = y_coordinate - shield_thickness_total

    # rate = distance / time = distance / (normal time + effective time)
    print(x_coordinate / (no_shield_region_height + shield_time_total))


def careful_ascent_binary_search():
    x_coordinate, y_coordinate = map(int, input().split())
    N = int(input())
    shield_region_widths = 0

    shields = []

    for _ in range(N):
        input_data = input().split()
        lower = int(input_data[0])
        upper = int(input_data[1])
        multiplier = float(input_data[2])
        thickness = upper - lower
        shield_region_widths += thickness

        shields.append((multiplier, thickness))

    no_shield_region_width = y_coordinate - shield_region_widths

    upper = 10**11
    lower = -10**11

    # Binary search for the velocity in the x-direction
    while lower < upper:
        velocity = (lower + upper) / 2

        # Calculate the distance traveled in the x-direction using `middle`
        distance = no_shield_region_width * velocity
        for multiplier, thickness in shields:
            distance += thickness * multiplier * velocity
        
        if distance < x_coordinate:
            lower = velocity + 0.0000001
        else:
            upper = velocity - 0.0000001

    print(lower)


from random import randint

# Either solution works
if randint(0, 1):
    careful_ascent_math()
else:
    careful_ascent_binary_search()
