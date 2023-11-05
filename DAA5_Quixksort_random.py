# Quicksort
# Randomized Quicksort

import random

# Function to partition the array
def partition_left(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

# Function to perform random partition
def partition_right(arr, low, high):
    r = random.randint(low, high)
    arr[r], arr[high] = arr[high], arr[r]
    return partition_left(arr, low, high)

# Recursive function for quicksort
def quicksort(arr, low, high):
    if low < high:
        p = partition_right(arr, low, high)
        quicksort(arr, low, p - 1)
        quicksort(arr, p + 1, high)

# Function to print the array
def print_array(arr):
    for item in arr:
        print(item, end=" ")
    print()

# Driver code
if __name__ == "__main__":
    arr = [6, 4, 12, 8, 15, 16]
    n = len(arr)

    print("Original array:", end=" ")
    print_array(arr)

    quicksort(arr, 0, n - 1)

    print("Sorted array:", end=" ")
    print_array(arr)
