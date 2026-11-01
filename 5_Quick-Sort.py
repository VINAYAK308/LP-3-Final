
import random
import time

# Deterministic Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    left = []
    right = []

    for i in arr[1:]:
        if i <= pivot:
            left.append(i)
        else:
            right.append(i)

    return quick_sort(left) + [pivot] + quick_sort(right)


# Randomized Quick Sort
def random_quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = random.choice(arr)

    left = []
    right = []

    for i in arr:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)

    equal = [i for i in arr if i == pivot]

    return random_quick_sort(left) + equal + random_quick_sort(right)


# Main Program
arr = list(map(int, input("Enter array elements: ").split()))

start = time.time()
a = quick_sort(arr.copy())
end = time.time()

print("Deterministic Quick Sort:", a)
print("Execution Time:", end - start)

start = time.time()
b = random_quick_sort(arr.copy())
end = time.time()

print("Randomized Quick Sort:", b)
print("Execution Time:", end - start)


# I/P: 
# Enter array elements: 45 23 89 12 67 34 10

# O/P:
# Deterministic Quick Sort: [10, 12, 23, 34, 45, 67, 89]
# Execution Time: 0.00001

# Randomized Quick Sort: [10, 12, 23, 34, 45, 67, 89]
# Execution Time: 0.00002

# Deterministic Quick Sort: Time – Best/Average: O(n log n), Worst: O(n²); Space – O(n).
# Randomized Quick Sort: Time – Expected: O(n log n), Worst: O(n²); Space – O(n).