def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def binary_search(arr, elem):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == elem:
            return mid
        elif arr[mid] < elem:
            left = mid + 1
        else:
            right = mid - 1
    return -1


unsorted_list = [4, 2, 1, 3, 5]
sorted_list = bubble_sort(unsorted_list)
print(sorted_list)

elem_to_find = 3
index = binary_search(sorted_list, elem_to_find)
if index != -1:
    print(f"Элемент {elem_to_find} найден в позиции {index}")
else:
    print(f"Элемент {elem_to_find} не найден в списке")
