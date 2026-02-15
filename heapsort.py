# Heapsort Implementation
# MSCS 532 - Assignment 4
# Based on concepts from CLRS (4th Edition)

def heapify(arr, n, i):
    largest = i            # Initialize largest as root
    left = 2 * i + 1       # Left child
    right = 2 * i + 2      # Right child

    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap

        # Recursively heapify the affected subtree
        heapify(arr, n, largest)


def heapsort(arr):
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap current root to end
        heapify(arr, i, 0)

    return arr

if __name__ == "__main__":
    test_array = [12, 11, 13, 5, 6, 7]
    print("Original array:", test_array)

    sorted_array = heapsort(test_array)
    print("Sorted array:", sorted_array)

