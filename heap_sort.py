'''
Heap sort -- time taken as a function of size  ==> size * log(size)  i.e. O(n log(n))

Build max heap from the input data such that the largest number is at the root node
Replace it with the last item in the heap, and also reduce the size of the heap by one.
With the new item in the root node, run heapify again.
The active list contains the unsorted numbers, with the largest number always at the root
And the sorted list continues to grow on the passive side of the list.
'''
def heap_sort(A, verbose=0, desc=0):
    import common as c

    # common routine to build the heap, and also to delete root
    def heapify(i, n):
        parent = i          # pointer of the parent node, that needs to be heap sorted
        ch_1 = i*2 + 1      # child #1
        ch_2 = ch_1 + 1     # child #2
        # check if index of child is within active range, and if it has lower/higher value
        while((ch_1 < n) and (A[ch_1] > A[parent])):
            parent = ch_1
        while((ch_2 < n) and (A[ch_2] > A[parent])):
            parent = ch_2
        if(verbose == 2): print("  sub:", i, n, " :: ", A)
        if(i != parent):
            A[i], A[parent] = c.swap(A[i], A[parent])
            heapify(parent, n-1)

    def h_sort():
        n = len(A)
        # building the heap  -- parent nodes = child nodes -1 (since each parent has 2 childs)
        # for n=7, there are 3 parent nodes (0, 1, 2) and 4 child nodes.
        for i in range((n // 2) - 1, -1, -1):      # just the parent nodes; 0 is a parent node
            heapify(i, n)
            if(verbose): print("iter #", i, " build  :: ", A)
        # deleting the root node. save the root node value at the end
        # build sorted list by decrementing the size of the list ...
        # sorted values beyond the end of the (active) list
        for i in range(n-1, 0, -1):
            A[0], A[i] = c.swap(A[0], A[i])
            heapify(0, i)
            if(verbose): print("iter #", i, " delete :: ", A)

    h_sort()
    if(desc): A = A[::-1]
    return(A)
