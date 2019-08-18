'''
A variant of Insertion sort. Since insertion sort compares numbers that are adjacent, there are
a lot of wasted operations, if the smaller numbers are further to the right. Shell sort addresses
it by comparing numbers that are much wider apart (defined by gap). It then logrithmically
reduces the gap, and eventually becomes 1. At which time the algorithm is the same as that
of Insertion Sort.

Shell sort -- time taken as a function of size  ==> size**2   i.e. O(n**2) -- worst case
'''


def shell_sort(A, verbose=0, desc=0):
    import common as c

    # using recursion
    def insertion_sort(gap, i=0):
        j, n = (gap + i), len(A)
        # index should be within range of the list
        if ((i < 0) or (j >= len(A))): return ()

        if(verbose == 2): print("  sub:", i, "-", j, " :: ", A)

        if (A[i] > A[j]):  # push larger numbers to the right
            A[i], A[j] = c.swap(A[i], A[j])
            insertion_sort(gap, i - gap)  # check previous set
        # note: when the above condition is true, i is pushed back to i - gap.
        # the cycle picks up again from this point, thus doing a few extra iterations.
        insertion_sort(gap, i + 1)  # increment i and j, recurse

    # start with a large enough gap, keep reducing until 0
    gap = len(A) // 2
    while (gap):
        if(verbose): print("gap  #", gap, " :: ", A)
        insertion_sort(gap, 0)  # gap = j - i
        gap = gap // 2
    if(desc): A = A[::-1]
    return (A)
