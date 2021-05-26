def quicksort(l,h):
    '''
    Using Quick sort Algorithm to sort the given array

    Parameter
    ---------
    l: (int)
    Lower index of the list.
    h: (int)
    Higher index of the list.

    Returns
    -------
    (list) Sorted Array
    '''
    if l<h:
        j = partion(l,h)
        quicksort(l,j)
        quicksort(j+1,h)
    return a


def partion(l,h):
    '''
    Partitioning the array and sorting the pivot element

    Parameter
    ---------
    l: (int)
    Lower index of the list.
    h: (int)
    Higher index of the list.

    Returns
    -------
    (int) The pivot index
    '''
    pivot = a[l]
    i = l
    j = h
    while i<j:
        while a[i] <= pivot:
            i += 1
        while a[j] > pivot:
            j -= 1
        if i < j:
            (a[i],a[j])=(a[j],a[i])
    (a[l],a[j])=(a[j],a[l])
    return j



# a = [17, 74, 102, 149, 398, 792, 797, 834, 987,float('inf')]
# print(quicksort(0,len(a)-1))