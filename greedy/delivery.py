N, capacity = map(int, input().split())

post_offices_positive = []
post_offices_negative = []

for _ in range(N):
    location, letters = map(int, input().split())
    if location > 0:
        post_offices_positive.append([location, letters])
    else:
        post_offices_negative.append([-1 * location, letters])

post_offices_positive.sort()
post_offices_negative.sort()

def solve(post_office):
    distance = 0
    N = len(post_office) - 1

    while N >= 0:
        carrying = capacity
        dest = post_office[N][0]
        delivery = post_office[N][1]
        distance += dest * 2

        if carrying < delivery: # Drop off as many letters as possible
            post_office[N][1] -= carrying
            continue
        elif carrying == delivery: # Drop off all letters and finish the current trip
            N -= 1
            continue
        else: # carrying > delivery, so we can drop off letters while heading back
            carrying -= delivery
            N -= 1

            while carrying > 0:
                if N < 0:
                    break

                delivery = post_office[N][1]

                if carrying < delivery: # Drop off as many letters as possible
                    post_office[N][1] -= carrying
                    break
                elif carrying == delivery: # Drop off all letters and finish the current trip
                    N -= 1
                    break
                else: # carrying > delivery, so we can drop off letters while heading back
                    carrying -= delivery
                    N -= 1

    return distance

# Solve for both positive and negative post offices
print(solve(post_offices_positive) + solve(post_offices_negative))
