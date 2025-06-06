def bubble_sort(arr):
    n = len(arr)
    # Outer loop for all passes
    for i in range(n):
        # Inner loop for each pair of adjacent elements
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Example usage
data = [64, 34, 25, 12, 22, 11, 90]
sorted_data = bubble_sort(data)
print("Sorted array:", sorted_data)


# 📌 Easy Explanation:
# Bubble sort compares two adjacent elements.

# If the left element is bigger, it swaps them.

# The biggest value "bubbles" to the end in each round.

#Time complexity is O(n^2) in worst case.