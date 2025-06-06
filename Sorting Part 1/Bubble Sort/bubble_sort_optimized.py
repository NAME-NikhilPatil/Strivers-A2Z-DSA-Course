def bubble_sort_optimized(arr):
    n = len(arr)
    for i in range(n):
        swapped = False  # Flag to check if any swapping happened

        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap the elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no swapping happened in the inner loop, array is sorted
        if not swapped:
            break
    return arr

# Example usage
data = [5, 1, 4, 2, 8]
sorted_data = bubble_sort_optimized(data)
print("Sorted array:", sorted_data)

#Time complexity is O(n^2) in worst case, but can be O(n) if the array is already sorted.
# ✅ Why is this better?
# If the list becomes sorted before all passes finish, it exits early.

# This makes it faster on nearly sorted data.
