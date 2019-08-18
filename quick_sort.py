'''
Quick sort -- time taken as a function of size
    - best ==> size  O(n.log(n))  worst ==> size**2 i.e. O(n**2)

Take a pivot element, any element (say the first element). Generate two sub-lists;
one that has numbers lower in value to the pivot. Another that has numbers higher in value.
Repeat process for the sublists.

'''
def quick_sort(A, verbose=0, desc=0):
    # use two pointers, one that moves right (increments, say i) and the other that moves left (j)
    # test the value at the pointer location against the pivot;
    # Keep moving while A[i] <= A[pivot]. Likewise while A[j] > A[pivot]
    # once both pointers stop moving, check if the pointers have crossed over.
    # If not, then swap the contents at the two pointer locations.
    # But, if yes, then swap the pivot with the end pointer (moving right to left)

    import common as c

    def partition(lb, ub):
        # initialize the pivot, and lower/upper bound
        pivot, start, end = A[lb], lb, ub
        while(start < end):
            while((A[start] <= pivot) and (start < ub)): start += 1
            while ((A[end] > pivot) and (end > lb)): end -= 1
            if(start < end):
                A[start], A[end] = c.swap(A[start], A[end])
            if(verbose == 2): print("  sub:", pivot, start, end, " :: ", A)
        A[lb], A[end] = c.swap(A[lb], A[end])
        return(end)

    # recursive call, partitioning the data along the location boundary
    def quick_sort(x, y):
        if(x < y):
            loc = partition(x, y)      # partition the data; smaller set, and higher set
            if(verbose): print("iter :", loc, x, y, " :: ", A)
            quick_sort(x, loc-1)       # recursive call on the smaller valued set
            quick_sort(loc+1, y)       # recursive call on the larger valued set

    quick_sort(0, len(A) -1)           # the initial call on the full list
    if(desc): A = A[::-1]
    return(A)
