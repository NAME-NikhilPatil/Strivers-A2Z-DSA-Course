def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key  # Place key at correct position

    return arr

# Example usage
data = [12, 11, 13, 5, 6]
sorted_data = insertion_sort(data)
print("Sorted array:", sorted_data)


# 📌 Easy Explanation:
# Think of sorting cards in your hand.

# You pick one card (key), and insert it in the correct position among the already sorted cards on the left.

# Repeat for all cards.

# Time complexity is O(n^2) in worst case, but can be O(n) if the array is already sorted.