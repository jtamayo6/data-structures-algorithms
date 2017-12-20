def mergeSortV1(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr)//2   # // is integer division in Python 3
    leftArr = mergeSort(arr[:mid])
    rightArr = mergeSort(arr[mid:])

    # Merge left and right sorted subarrays
    sortedArr = []
    l = 0
    r = 0
    while l < len(leftArr) and r < len(rightArr):
        if leftArr[l] <= rightArr[r]:
            sortedArr.append(leftArr[l])
            l += 1
        else:
            sortedArr.append(rightArr[r])
            r += 1
    if l == len(leftArr):
        sortedArr += rightArr[r:]
    else:
        sortedArr += leftArr[l:]

    return sortedArr


# mergeSortV2() uses the input array to store sorted subarrays
# So it uses less space than mergeSortV1()
def mergeSortV2(arr, low, high):  # [low, high)
    if low == high-1:
        return

    mid = (low + high)//2   # // is integer division in Python 3
    mergeSort(arr, low, mid)
    mergeSort(arr, mid, high)

    # Merge left and right sorted subarrays
    sortedArr = []
    l = low
    r = mid
    while l < mid and r < high:
        if arr[l] <= arr[r]:
            sortedArr.append(arr[l])
            l += 1
        else:
            sortedArr.append(arr[r])
            r += 1
    if l == mid:
        sortedArr += arr[r:high]
    else:
        sortedArr += arr[l:mid]

    for i, j in enumerate(range(low, high)):
        arr[j] = sortedArr[i]

    return


if __name__ == "__main__":
    arr = [7, 4, 10, 2, 5, 1, 14, -3, 11, -5]
    print("Unsorted arr =", arr)

    # sortedArr = mergeSortv1(arr)
    # print("Sorted arr = ", sortedArr)

    mergeSortv2(arr, 0, len(arr))
    print("Sorted arr = ", arr)
