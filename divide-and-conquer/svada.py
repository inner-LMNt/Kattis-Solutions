time = int(input())

N = int(input())
monkeys_A = []
for i in range(N):
    monkeys_A.append(input().split())

M = int(input())
monkeys_B = []
for i in range(M):
    monkeys_B.append(input().split())

upper_time = time
lower_time = 0
A_time = 0

# Because we can quickly verify a potential time, use BSTA
while lower_time < upper_time:
    A_time = (lower_time + upper_time) // 2
    B_time = time - A_time
    coconuts = 0

    # Calculate how many coconuts are gathered by all A-type monkeys
    for monkey in monkeys_A:
        if A_time >= int(monkey[0]):
            coconuts += 1 + (A_time - int(monkey[0])) // int(monkey[1])

    # Calculate how many coconuts are opened by all B-type monkeys
    for monkey in monkeys_B:
        if B_time >= int(monkey[0]):
            coconuts -= 1 + (B_time - int(monkey[0])) // int(monkey[1])

    if coconuts > 0: # too many coconuts remaining
        upper_time = A_time
    elif coconuts < 0: # too few
        lower_time = A_time + 1
    else:
        break

result = 0
excess = 10000000000 # worst case
mid_time = (lower_time + upper_time) // 2

# After breaking from BSTA, check `mid_time - 1` and `mid_time`
# This is because using just `mid_time` can sometimes result in too many coconuts
for i in [mid_time - 1, mid_time]:
    A_time = i
    B_time = time - i
    coconuts = 0

    for monkey in monkeys_A:
        if A_time >= int(monkey[0]):
            coconuts += 1 + (A_time - int(monkey[0])) // int(monkey[1])

    for monkey in monkeys_B:
        if B_time >= int(monkey[0]):
            coconuts -= 1 + (B_time - int(monkey[0])) // int(monkey[1])

    # Valid net coconuts and minimum excess
    if coconuts <= 0 and -coconuts < excess:
        result = A_time

print(result)
