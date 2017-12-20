def mergeSort(arr):
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

if __name__ == "__main__":
    arr = [7, 4, 10, 2, 5, 1, 14, -3, 11, -5]
    print("Unsorted arr =", arr)

    sortedArr = mergeSort(arr)
    print("Sorted arr = ", sortedArr)