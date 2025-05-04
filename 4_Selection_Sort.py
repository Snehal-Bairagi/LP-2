def selectionSort(arr):
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

# Main function
if __name__ == '__main__':
    arr = list(map(int, input("Enter the elements separated by space: ").split()))
    print("Original array:", arr)
    sorted_arr = selectionSort(arr)
    print("Sorted array:", sorted_arr)

# 📌 Sample Input:
# Enter the elements separated by space: 64 25 12 22 11
#
# ✅ Output:
# Original array: [64, 25, 12, 22, 11]
# Sorted array:   [11, 12, 22, 25, 64]