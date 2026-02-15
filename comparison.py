import random
import time
from heapsort import heapsort

def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)
def mergesort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = mergesort(arr[:mid])
    right_half = mergesort(arr[mid:])

    return merge(left_half, right_half)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

def measure_time(sort_function, arr):
    start_time = time.perf_counter()
    sort_function(arr.copy())
    end_time = time.perf_counter()
    return end_time - start_time

if __name__ == "__main__":

    sizes = [1000, 5000, 10000]

    for size in sizes:
        print(f"\nInput Size: {size}")

        # Random data
        random_data = [random.randint(1, 100000) for _ in range(size)]

        # Sorted data
        sorted_data = list(range(size))

        # Reverse sorted data
        reverse_data = list(range(size, 0, -1))

        for data_type, data in [("Random", random_data),
                                ("Sorted", sorted_data),
                                ("Reverse", reverse_data)]:

            print(f"\nData Type: {data_type}")

            heap_time = measure_time(heapsort, data)
            quick_time = measure_time(quicksort, data)
            merge_time = measure_time(mergesort, data)

            print(f"Heapsort Time: {heap_time:.6f} seconds")
            print(f"Quicksort Time: {quick_time:.6f} seconds")
            print(f"Merge Sort Time: {merge_time:.6f} seconds")


