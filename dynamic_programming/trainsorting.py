num = int(input())

if num >= 0 and num <= 3: # easy cases
    for i in range(num):
        input()
    print(num)
    exit()

trains = []
for i in range(num):
    train = int(input())
    trains.append(train)

longest_increasing = [1 for _ in range(num)]
# longest_increasing[i] is the length of the LIS starting from the i-th train
for i in reversed(range(num)):
    for j in range(num - 1, i, -1):
        if trains[i] < trains[j]:
            longest_increasing[i] = max(longest_increasing[i], longest_increasing[j] + 1)

longest_decreasing = [1 for _ in range(num)]
# longest_decreasing[i] is the length of the LDS starting from the i-th train
for i in reversed(range(num)):
    for j in range(num - 1, i, -1):
        if trains[i] > trains[j]:
            longest_decreasing[i] = max(longest_decreasing[i], longest_decreasing[j] + 1)

result = 1

# The longest bitonic subsequence is of the form: LDS[i] <-> initial train <-> LIS[i]
# We can iterate through choosing each train to be the first train selected to be in the sequence
for i in range(num):
    result = max(result, longest_increasing[i] + longest_decreasing[i] - 1)

print(result)