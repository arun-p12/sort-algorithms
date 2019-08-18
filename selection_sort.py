'''
Selection sort -- time taken as a function of size  ==> size**2   i.e. O(n**2)

Iterate thru each iter location starting from 0. From that location to the end of the list,
find the minimum/maximum. Swap the element in the index location with the iter location.
Increment iter position, recurse thru the remainder of the list (which decrements size by one).
'''
def selection_sort(A, verbose=0, desc=0):
    import common as c

    def s_sort(A):
        n = len(A)
        if(n <= 1): return(A)

        val, index = c.minimum(A)   # the inner iterative loop!
        A[index] = A[0]             #
        if(verbose): print("iter #:", n-1, " :: ", [val ] + A[1::])
        return([val] + s_sort(A[1::]) )     # the outer iterative loop!

    A = s_sort(A)
    if (desc): A = A[::-1]
    return (A)