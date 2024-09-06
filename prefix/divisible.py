from collections import defaultdict

test_cases = int(input())

for _ in range(test_cases):
    divisor, length = map(int, input().split())
    numbers = list(map(int, input().split()))

    running_mod_sum = 0
    prefix_mod = defaultdict(int) # frequency of each prefix sum modulo divisor
    for i in range(length):
        running_mod_sum = (running_mod_sum + numbers[i]) % divisor
        prefix_mod[running_mod_sum] += 1

    result = 0

    # Special case where the subarray starts at index 0
    if prefix_mod[0] > 0:
        result += prefix_mod[0]

    # We can make divisible subarrays by choosing start and end points with the same prefix sum modulo
    for key, value in prefix_mod.items():
        if value == 1:
            continue

        # nC2 = n! / (2! * (n-2)!)
        result += ((value) * (value - 1)) // 2

    print(result)