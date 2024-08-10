test_num, length = map(int, input().split())

tests = []
for i in range(test_num):
    # Convert each answer string to a binary list
    test = []
    data = input()
    for j in range(length):
        if data[j] == 'T':
            test.append(1)
        else:
            test.append(0)
    tests.append(test)

# Complete search over all answer keys (2^length possibilities)
bitmap = 2**length

maximum = 0
for i in range(bitmap): # `i` is a potential answer key
    potential_worst = length

    for test in tests:
        score = length # assume perfect score at first
        for j in range(length):
            answer = 1 << j # get the jth question

            if not (i & answer) and test[j]: # key says false, answered true
                score -= 1
            elif (i & answer) and not test[j]: # key says true, answered false
                score -= 1

        potential_worst = min(potential_worst, score)

    maximum = max(maximum, potential_worst)

print(maximum)
