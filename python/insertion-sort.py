def insertionsort(arr):
    '''
    Using Insertion sort Algorithm to sort the given array

    Parameter
    ---------
    arr: (list)
    The array which is to be sorted.

    Returns
    -------
    (list) Sorted Array
    '''
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and key<arr[j]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
            j -= 1

    return arr


if __name__ == "__main__":
    a = [17, 74, 9, 149, 398, 792, 7128, 834, 987]
    print(insertionsort(a))