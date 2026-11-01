# PRACTICAL 3: HUFFMAN ENCODING

# Aim: Implement Huffman Encoding using a greedy
# strategy.

# Program:

import heapq

def huffman_encoding(data):
    heap = []

    for char, freq in data.items():
        heap.append([freq, [char, ""]])
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        for item in left[1:]:
            item[1] = "0" + item[1]

        for item in right[1:]:
            item[1] = "1" + item[1]

        heapq.heappush(
            heap, [left[0] + right[0]]
            + left[1:] + right[1:]
        )

    return sorted(heap[0][1:], key=lambda x: x[0])

n = int(input("Enter number of characters: "))
data = {}

for i in range(n):
    char = input("Enter character: ")
    freq = int(input("Enter frequency: "))
    data[char] = freq

codes = huffman_encoding(data)

print("\nCharacter : Huffman Code")
for char, code in codes:
    print(char, ":", code)

# Input:
# Enter number of characters: 3

# Enter character: A
# Enter frequency: 5

# Enter character: B
# Enter frequency: 9

# Enter character: C
# Enter frequency: 12

# Output:
# Character : Huffman Code
# A : 10
# B : 11
# C : 0

# Time Complexity: O(n log n)
# Space Complexity: O(n)




# Aim: Implement Huffman Encoding using Greedy Strategy without using the heapq module.

def huffman_encoding_heapq(data):

    heap = [[freq, [char, ""]]
            for char, freq in data.items()]

    while len(heap) > 1:

        heap.sort()

        left = heap.pop(0)
        right = heap.pop(0)

        for item in left[1:]:
            item[1] = "0" + item[1]

        for item in right[1:]:
            item[1] = "1" + item[1]

        new_node = [left[0] + right[0]] + left[1:] + right[1:]

        heap.append(new_node)

    return sorted(heap[0][1:], key=lambda x: x[0])


n = int(input("Enter number of characters: "))
data = {}

for i in range(n):
    char = input("Enter character: ")
    freq = int(input("Enter frequency: "))
    data[char] = freq

codes = huffman_encoding_heapq(data)

print("\nCharacter : Huffman Code")

for char, code in codes:
    print(char, ":", code)