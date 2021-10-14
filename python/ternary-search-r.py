def ternarysearchr(arr,element,l,h):
    '''
    Using Ternary Search to find the element in list.
    Method: recursive

    Parameter
    ---------
    arr: (list)
    A sorted list on which we are going to apply ternary search
    
    element: (any)
    The element which we are searching for in the list

    l: (int)
    The lower index of the list

    h: (int)
    The higher index of the list

    Returns
    -------
    (int) Index of element if found else None
    '''
    if h >= l:
        mid1 = l + (h-l) // 3
        mid2 = h - (h-l) // 3

        if arr[mid1] == element:
            return mid1
        if arr[mid2] == element:
            return mid2

        if arr[mid1] > element:
            return ternarysearchr(arr, element, l, mid1-1)
        elif arr[mid2] < element:
            return ternarysearchr(arr, element, mid2+1, h)
        else:
            return ternarysearchr(arr, element, mid1+1, mid2-1)

    return None

if __name__ == "__main__":
    l = [17, 74, 102, 149, 398, 792, 797, 834, 987]
    print(ternarysearchr(l,1,0,len(l)-1))
