def bubbleSort(arr):
    n = len(arr)
    swapped = True

    while swapped:
        swapped = False
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                swapped = True
                # print(arr)

    return arr

if __name__ == "__main__":
    arr = [7, 4, 10, 2, 5, 1, 14, -3, 11, -5]
    print("Unsorted arr =", arr)

    sortedArr = bubbleSort(arr)
    print("Sorted arr = ", sortedArr)