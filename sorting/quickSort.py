def quickSort(arr, left, right):
    index = partition(arr, left, right)
    if left < index - 1:
        quickSort(arr, left, index - 1)
    if right > index:
        quickSort(arr, index, right)


def partition(arr, left, right):
    pivot = arr[left + (right-left)//2]
    while left <= right:
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return left

if __name__ == "__main__":
    arr = [7, 4, 10, 2, 5, 1, 14, -3, 11, -5]
    print("Unsorted arr =", arr)

    quickSort(arr, 0, len(arr)-1)
    print("Sorted arr = ", arr)