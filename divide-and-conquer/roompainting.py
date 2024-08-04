sizes_offered, colors_needed = map(int, input().split())

sizes = []
for _ in range(sizes_offered):
    sizes.append(int(input()))

sizes.sort()

# Binary search, but if the item is not found then return the next largest value
def binary_search_least_greater(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid # size found
        elif array[mid] < target:
            left = mid + 1 # if while loop broken here, left is the index of the next largest
        else:
            right = mid - 1 # if while loop broken here, left is also the index of the next largest

    return left # not found, choose next largest

count = 0

for i in range(colors_needed):
    color = int(input())
    index = binary_search_least_greater(sizes, color)
    count += sizes[index] - color

print(count)
