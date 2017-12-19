def binarySearchRec(arr, key, low, high):
    if low > high:
        return -1

    mid = (low + high)//2   # // is integer division in Python 3
    if key == arr[mid]:
        return mid
    elif key < arr[mid]:
        return binarySearchRec(arr, key, low, mid-1)
    else:   # key > arr[mid]
        return binarySearchRec(arr, key, mid+1, high)


def binarySearchIter(arr, key):
    low = 0
    high = len(arr) - 1

    while low < high:
        mid = (low + high)//2
        if key == arr[mid]:
            return mid
        elif key < arr[mid]:
            high = mid-1
        else:   # key > arr[mid]
            low = mid+1

    return -1   # low > high


if __name__ == "__main__":
    arr = [3, 7, 11, 16, 21, 23, 28, 32, 33, 40, 57, 59, 65]
    print("arr =", arr)
    print("Index of 11 is:", binarySearchRec(arr, 11, 0, len(arr)-1))
    print("Index of 59 is:", binarySearchRec(arr, 59, 0, len(arr)-1))
    print("Index of 20 is:", binarySearchRec(arr, 20, 0, len(arr)-1)) # Should be -1 (not found)

    print("Index of 21 is:", binarySearchIter(arr, 21))
    print("Index of 59 is:", binarySearchIter(arr, 40))
    print("Index of 35 is:", binarySearchIter(arr, 35)) # Should be -1 (not found)