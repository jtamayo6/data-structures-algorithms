
# Get length of longest increasing subsequence
# def LIS(arr):
#     if arr == []:
#         return 0
#     L = [1]
#
#     for i in range(1, len(arr)):
#         L.append(0)
#         for j in range(i):
#             if arr[j] < arr[i] and L[i] < L[j]+1:
#                 L[i] = L[j]
#         L[i] += 1
#     return L[-1]


# Get actual subsequences
# def LIS(arr):
#     import copy
#     L = [[arr[0]]]  # [ [arr[0]], ...]
#
#     for i in range(1, len(arr)):
#         L.append([])
#         for j in range(i):
#             if arr[j] < arr[i] and len(L[i]) < len(L[j])+1:
#                 L[i] = copy.deepcopy(L[j])
#         L[i].append(arr[i])
#     return L


# O(n log n) solution
# Borrowed from https://stackoverflow.com/questions/2631726/how-to-determine-the-longest-increasing-subsequence-using-dynamic-programming
def getCeilIndex(arr, subsequence, currIndex):
    # Returns the index of the smallest value in subsequence as big as arr[elem].
    # arr[elem] must not be larger than every element in subsequence.
    # The elements in subsequence are indices in sequence.
    # Uses binary search.

    low = 0
    high = len(subsequence) - 1

    while high > low:
        mid = (high + low)//2                                                           
        if arr[subsequence[mid]] < arr[currIndex]:
            low = mid + 1                                         
        else:
            high = mid

    return high

def LIS(arr):
    # smallestTailsOfSubsequence[i] = index of element for longest subsequence of length i
    smallestTailsOfSubsequence = []

    # parent[i] = index of "parent" element (next smallest element in sequence) for i-th element in arr
    parent = [None for _ in range(len(arr))]

    for i in range(len(arr)):
        # If True, then the first LIS of length x+1 has been found
        if len(smallestTailsOfSubsequence) == 0 or arr[i] > arr[smallestTailsOfSubsequence[-1]]:
            # If not the first element, set the parent to be the tail element of the next shortest LIS
            if len(smallestTailsOfSubsequence) > 0:
                parent[i] = smallestTailsOfSubsequence[-1]
            smallestTailsOfSubsequence.append(i)
        else:
            # Find where this element can replace the tail element of an LIS
            indexOfElemToReplace = getCeilIndex(arr, smallestTailsOfSubsequence, i)
            smallestTailsOfSubsequence[indexOfElemToReplace] = i
            # Update parent if the LIS being updated is not of length 1
            if indexOfElemToReplace != 0:
                parent[i] = smallestTailsOfSubsequence[indexOfElemToReplace - 1]

    # Generate the longest increasing subsequence by backtracking through parent.
    currParent = smallestTailsOfSubsequence[-1]
    L = []

    while currParent is not None:
        L.insert(0, arr[currParent])
        currParent = parent[currParent]

    return L


if __name__ == "__main__":
    arr = [15, 27, 14, 38, 26, 55, 46, 65, 85]
    print(arr)

    print(LIS(arr))

    # L = LIS(arr)
    # for l in L:
    #     print(l)