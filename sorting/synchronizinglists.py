while True:
    n = int(input())
    if n == 0:
        break

    first_list = []
    for _ in range(n):
        first_list.append(int(input()))

    second_list = []
    for _ in range(n):
        second_list.append(int(input()))

    first_list_sorted = first_list.copy()
    second_list_sorted = second_list.copy()

    # As per problem statement, the two lists correspond item by item when sorted
    first_list_sorted.sort()
    second_list_sorted.sort()

    for num in first_list:
        # item in first_list -> its index in first_list_sorted -> corresponding item in second_list_sorted
        print(second_list_sorted[first_list_sorted.index(num)])

    print()
