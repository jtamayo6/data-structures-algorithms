def insertionSort(arr):
    for i in range(1, len(arr)):
        j = i
        temp = arr[i]
        while j > 0 and arr[j-1] > temp:
            arr[j] = arr[j-1]
            j -= 1
            # print(i, j, arr)
        arr[j] = temp

    return arr

if __name__ == "__main__":
    arr = [7, 4, 10, 2, 5, 1, 14, -3, 11, -5]
    print("Unsorted arr =", arr)

    sortedArr = insertionSort(arr)
    print("Sorted arr = ", sortedArr)