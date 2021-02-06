def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0] # 2
    left = list(filter(lambda x: x < pivot, arr))
    center = [x for x in arr if x == pivot]
    right = []
    for x in arr:
        if x > pivot:
            right.append(x)
    return quick_sort(left) + center + quick_sort(right) # [1]


arr = [6, 2, 4, 1, 9, 9, 6, 7, 6]
print(quick_sort(arr))
