num = int(input())
nums = list(map(int, input().split()))

# maximums[i] = max(nums[0], nums[1], ..., nums[i])
maximums = []
for i in range(num):
    maximums.append(nums[i])

running_max = nums[0]
for i in range(1, num):
    maximums[i] = running_max
    running_max = max(running_max, nums[i])
   
# minimums[i] = min(nums[num - 1], nums[num - 2], ..., nums[i])
minimums = []
for i in range(num):
    minimums.append(nums[i])

running_min = nums[-1]
for i in range(num - 2, -1, -1):
    minimums[i] = running_min
    running_min = min(running_min, nums[i])
    
# A valid pivot, n, is such that every element to the left is <= n and every element to the right is > n
result = 0
for i in range(1, num - 1):
    if maximums[i] <= nums[i] and minimums[i] > nums[i]:
        result += 1

# Check the ends of the array
if nums[0] <= minimums[0]:
    result += 1

if nums[-1] >= maximums[-1]:
    result += 1

print(result)