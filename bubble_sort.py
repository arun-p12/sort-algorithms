'''
Bubble sort -- time taken as a function of size  ==> size**2 i.e. O(n**2)

Take two adjacent elements, and swap them if required. Repeat process, until end of list.
The last element of the list would now contain the requried value.
Repeat for N - 1 iterations. But, in each iteration the list size reduces since the last
element is already sorted.

To futher optimize, check if in a pass, there has been no swapping. If true, then it means the
list is already sorted, and we can stop right at the end of that pass.
'''
def bubble_sort(A, verbose=False, asc=True):
    import common as c
    for i in range(len(A)):
        swapped = 0
        for j in range(len(A) -1 - i):
            if(A[j] > A[j+1]):
                (A[j], A[j+1]) = c.swap(A[j], A[j+1])
                swapped = 1
        if(verbose): print("iter #", i, " :: ", A)
        if(not swapped): break
    if(not asc): A = A[::-1]
    return(A)

