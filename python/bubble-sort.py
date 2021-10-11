def bubblesort(arr):
    '''
    Using Bubble sort Algorithm to sort the given array

    Parameter
    ---------
    arr: (list)
    The array which is to be sorted.

    Returns
    -------
    (list) Sorted Array
    '''
    for i in range(len(arr)):
        for j in range(len(a)-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr


if __name__ == "__main__":
    a = [17, 74, 9, 149, 398, 792, 7128, 834, 987]
    print(bubblesort(a))