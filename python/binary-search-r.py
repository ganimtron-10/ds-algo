import math

def binarysearchr(arr,element,l,h):
    '''
    Using Binary Search to find the element in list.
    Method: recursive

    Parameter
    ---------
    arr: (list)
    A sorted list on which we are going to apply binary search
    
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
    if l==h:
        if arr[l] == element:
            return l
        else:
            return None
    else:
        mid = math.floor((l+h)/2)
        if arr[mid] == element:
            return mid
        elif arr[mid] > element:
            return binarysearchr(arr,element,l,mid-1)
        elif arr[mid] < element:
            return binarysearchr(arr,element,mid+1,h)


if __name__ == "__main__":
    l = [17, 74, 102, 149, 398, 792, 797, 834, 987]
    print(binarysearchr(l,987,0,len(l)-1))
