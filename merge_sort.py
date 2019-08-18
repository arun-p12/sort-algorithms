'''
time taken as a function of size  ==> worst: size * log(size) i.e. O(n.log(n))

Anology: Sorting cards ... Two heaps of cards, with each heap sorted, being merged into a
sorted pile. Check the two top cards, pick the smaller valued card. That will be the smallest.
Check the two cards that's topmost now. Move the smallest to the sorted pile. Keep repeating.

To get the two piles to be sorted in the first place, recurse. Break each of the two piles into
two piles each, and then into two each more etc, until each pile has only one card. Sort and merge
'''
def merge_sort(A, verbose=0, desc=0):

    def merge(lb, mid, ub):
        # the top pointers for the two halves, and the index location in the B array
        i, j, k = lb, mid+1, lb
        B = [0] * (ub + 1)                  # temporary placeholder for the sorted items
        while((i <= mid) and (j <= ub)):    # while neither of the two sets are empty
            if(A[i] <= A[j]):               # is the topmost in the left pile smaller?
                B[k] = A[i]                 # save it in the temporary array
                i += 1                      # update pointer
            else:
                B[k] =  A[j]
                j += 1
            k += 1
            #if (verbose == 2): print("  sub:", mid, "(mid)", " :: ", B)
        # only one of two below will execute
        while(i <= mid):                    # Is this array that still has items
            B[k] = A[i]                     # if yes, drain the items in it
            i += 1
            k += 1
        while (j <= ub):
            B[k] = A[j]
            j += 1
            k += 1
        # update the main list with the sorted values
        for k in range(lb, len(B)):         # go from lb to ub
            A[k] = B[k]
        if (verbose == 2):
            print("    B:", lb, "-", ub, " :: ", B)
            print("    A:", lb, "-", ub, " :: ", A)

    # divide into two (equal) halves. Recurse. Merge the two sorted halves
    def merge_sort(low, high):
        if(low < high):
            mid = (low + high) // 2
            merge_sort(low, mid)            # the left half
            merge_sort(mid+1, high)         # the right half
            merge(low, mid, high)           # merge the two
            if(verbose): print("iter :", low, "-", high, " :: ", A)
    merge_sort(0, len(A) -1)
    if(desc): A = A[::-1]
    return(A)
