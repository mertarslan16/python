def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Input list
lst = [22, 27, 16, 2, 18, 6]

print("Original list:", lst)
insertion_sort(lst)
print("Sorted list:", lst)