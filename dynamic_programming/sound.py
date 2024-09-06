from heapq import heappush, heappop
from collections import defaultdict

samples, length, max_noise = map(int, input().split())
sample = list(map(int, input().split()))

# dp_min[i] = minimum of subarray [i: i + length - 1]
# dp_max[i] = maximum of subarray [i: i + length - 1]
dp_min = [1000000] * (samples - length + 1)
dp_max = [0] * (samples - length + 1)

min_heap = [] # min heap for running subarray
max_heap = [] # max heap for running subarray

# occurrences[i] = number of times i appears in the running subarray
occurrences = defaultdict(int)

# Initialize heaps and occurrences for the first subarray
for i in range(length):
    occurrences[sample[i]] += 1

    heappush(min_heap, sample[i])
    heappush(max_heap, -sample[i])

dp_min[0] = min_heap[0]
dp_max[0] = -max_heap[0]

# Sliding window
for i in range(length, samples):
    occurrences[sample[i]] += 1 # newly added

    removed_item = sample[i - length] # pushed out of window range
    occurrences[removed_item] -= 1 # can create "tombstone" elements that are not in the current subarray, but still in the heap

    current_max = -max_heap[0]
    current_min = min_heap[0]    

    # Clean up least number of tombstone elements that affect the current max and min
    while occurrences[-max_heap[0]] == 0:
        heappop(max_heap)

    while occurrences[min_heap[0]] == 0:
        heappop(min_heap)

    heappush(min_heap, sample[i])
    heappush(max_heap, -sample[i])

    dp_min[i - length + 1] = min_heap[0]
    dp_max[i - length + 1] = -max_heap[0]      

result = []

# Check silence conditions
for i in range(samples - length + 1):
    if dp_max[i] - dp_min[i] <= max_noise:
        result.append(i + 1) # problem is 1-indexed for some reason

if len(result) == 0:
    print('NONE')
    exit()

for i in result:
    print(i)