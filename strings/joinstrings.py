# Linked list solution
# Node class to store the string itself and string after it
class Node:
    def __init__(self, word):
        self.word = word
        self.next = None

# Used to concatenate the strings by linking the end of the first string to the start of the second string
def concatenate(a, b):
    string_lists_end[a].next = string_lists[b]
    string_lists_end[a] = string_lists_end[b]
    string_lists[b] = None

N = int(input())
string_lists = [None] * N
string_lists_end = [None] * N # Store the end of each string

# Gather the strings
for i in range(N):
    word = input()
    node = Node(word)
    string_lists[i] = node
    string_lists_end[i] = node

# Run through the operations
for _ in range(N-1):
    data = input().split()
    a = int(data[0])-1
    b = int(data[1])-1
    concatenate(a, b)

# Print the combined string
# Include a case for N = 1
if (N != 1):
    current = string_lists[a]
    while current:
        print(current.word, end='')
        current = current.next
else:
    print(string_lists[0].word)
