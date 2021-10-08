def selectionsort(arr):
    '''
    Using Selection sort Algorithm to sort the given array

    Parameter
    ---------
    arr: (list)
    List which is to be sorted

    Returns
    -------
    (list) Sorted Array
    '''
    h = len(arr)-1
    for i in range(h):
        l = i + 1
        while(l<=h):
            if arr[i] > arr[l]:
                arr[i],arr[l] = arr[l],arr[i]
            l+=1
    return arr


if __name__ == "__main__":
    a = [i for i in range(100)]
    print(selectionsort(a))