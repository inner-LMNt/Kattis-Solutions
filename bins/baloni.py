from collections import defaultdict

N = int(input())
balloons = list(map(int, input().split()))
height_bins = defaultdict(int)
result = 0

for i in range(N):
    height = balloons[i]

    # At least one arrow is needed to hit the current balloon and will it continue at that height.
    height_bins[height] += 1

    # Any arrow with height+1 in height_bins will come before the current balloon because of iteration.
    if height_bins[height + 1] > 0:
        height_bins[height + 1] -= 1 # Use up a previous arrow.
        continue # We don't need a new arrow right now.

    # If we reach here, a new arrow will have to be fired, adding to the result.
    result += 1

print(result)
