def linearsearch(arr,element):
    '''
    Using Linear Search to find the element in list.
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
    for i in range(len(arr)):
        if arr[i] == element:
            return i
    return None

if __name__ == "__main__":
    l = [1, 2, 54, 56, 63, 64, 75, 84, 86, 543, 987, 2624, 2665]
    print(linearsearch(l,2))