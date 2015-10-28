#!/usr/bin/env python3

def index_power(array, n):
    """
        Find Nth power of the element with index N.
    """
    lenarr = len(array) - 1
    if (n>lenarr or n<0):
        #print("n=",n,"la=",lenarr)
        #print (-1)
        return -1
    else:
        #print("n=",n,"la=",lenarr)
        #print (array[n]**n)
        return array[n]**n


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert index_power([1, 2, 3, 4], 2) == 9, "Square"
    assert index_power([1, 3, 10, 100], 3) == 1000000, "Cube"
    assert index_power([0, 1], 0) == 1, "Zero power"
    assert index_power([1, 2], 3) == -1, "IndexError"
    #index_power([1, 2, 3, 4], 2)
    #index_power([1, 3, 10, 100], 3)
    #index_power([0, 1], 0)
    #index_power([1, 2], 3)
