def merge(arr1,arr2):
    '''
    Mergers the given two list in sorted manner

    Parameter
    ---------
    arr1: (list)
    First list to be merged

    arr1: (list)
    Second list to be merged

    Returns
    -------
    (list) Merged Array
    '''
    i = j = 0
    mergedarr = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            mergedarr.append(arr1[i])
            i += 1
        else:
            mergedarr.append(arr2[j])
            j += 1
    for n in range(i,len(arr1)):
        mergedarr.append(arr1[n])
    for m in range(j,len(arr2)):
        mergedarr.append(arr2[m])
    return mergedarr

def mergesort(arr):
    '''
    Using Merge sort Algorithm to sort the given array

    Parameter
    ---------
    arr: (list)
    The list to be sorted.

    Returns
    -------
    (list) Sorted Array
    '''
    mid = len(arr)//2
    left,right = arr[:mid],arr[mid:]
    if len(left)>1:
        left = mergesort(left)
    if len(right) > 1:
        right = mergesort(right)
    return merge(left,right)
        

# l = [48,79,12,29,20,78,34,64,86,23]
# print(mergesort(l))