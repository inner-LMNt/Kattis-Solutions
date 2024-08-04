n, m, a, c, x_0 = map(int, input().split())

def next_x(x):
    return (a * x + c) % m

current_x = next_x(x_0)

sequence = []

# Generate the sequence according to the problem statement
for i in range(n):
    sequence.append(current_x)
    current_x = (a * current_x + c) % m

# Check if a number is able to be found using binary search
def binary_searchable(left, right, number):
    if left > right:
        return False
    middle = (left + right) // 2
    if sequence[middle] == number:
        return True
    elif sequence[middle] > number:
        return binary_searchable(left, middle - 1, number)
    else:
        return binary_searchable(middle + 1, right, number)
    
result = 0
middle_index = (n - 1) // 2

for i in range(0, middle_index):
    if sequence[i] > sequence[middle_index]: # Cannot be found; too large
        continue
    else:
        if binary_searchable(0, middle_index - 1, sequence[i]):
            result += 1

result += 1 # Middle element is always binary searchable

for i in range(middle_index + 1, n):
    if sequence[i] < sequence[middle_index]: # Cannot be found; too small
        continue
    else:
        if binary_searchable(middle_index + 1, n - 1, sequence[i]):
            result += 1        

print(result)
