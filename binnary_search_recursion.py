def binary_search(arr, start, finish, target):
    mid = (start + finish) // 2
    mid_num = arr[mid]

    if start > finish:
        return None

    if mid_num == target:
        return mid
    elif target < mid_num:
        finish = mid - 1
        return binary_search(arr, start, finish, target)
    else:
        start = mid + 1
        return binary_search(arr, start, finish, target)


a = [2, 5, 7, 7483, 9, 342, 8, 6, 99, 10]
print(binary_search(a, 0, len(a) - 1, 99))
