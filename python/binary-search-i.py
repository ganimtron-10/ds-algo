import math

def binarysearchi(arr,element):
    '''
    Using Binary Search to find the element in list.
    Method: iterative

    Parameter
    ---------
    arr: (list)
    A sorted list on which we are going to apply binary search
    
    element: (any)
    The element which we are searching for in the list

    Returns
    -------
    (int) Index of element if found else None
    '''
    l = 0
    h = len(arr)
    while l<h:
        mid = math.floor((l+h)/2)
        if arr[mid] == element:
            return mid
        elif arr[mid] > element:
            h = mid - 1
        elif arr[mid] < element:
            l = mid + 1
    else:
        return None


# l = [1, 2, 54, 56, 63, 64, 75, 84, 86, 543, 987, 2624, 2665]
# print(binarysearchi(l,2665))