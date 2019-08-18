'''
time taken as a function of size  ==> size**2 i.e. O(n**2)

Anology: sorting cards... Start with empty left hand, pick a card, from an unsorted pile on
the table. insert into hand. New card inserted goes to the sorted location, shifting the index
of other cards appropriately.

In the worst case scenario when every check of A[i] > key is true, the while loop for i = 3
runs 3 times, for i = 10, runs 10 times etc.
Thus the total computational steps = 1 + 2 + 3 + .... + n = n(n+1)/2 = (n**2 + n)/2

More generally, the overall equation can be represented as a*n**2 + b*n + c .... a quadratic eqn.
For very large values of n, the lower order terms (bn and c) and constant 'a' can be ignored.
Leaving us with the execution time being controlled by n**2
'''


# items A[0 ... i-1] is the sorted pile in hand. A[i] is the top card from the unsorted pile.
# A[i+1 ... n] is the remaining unsorted pile face down on the table.
def insertion_sort(A, verbose=0, desc=0):
    for i in range(1, len(A)):         # until we know better the 0th element is ok
        key = A[i]                     # save the entity we are interested in
        j = i - 1
        while ((j >= 0) and (A[j] > key)):  # check if key is smaller ... go right to left
            A[j+1] = A[j]              # update the right (higher index) with the correct value
            j -= 1
            if (verbose == 2): print("  sub:", j, " :: ", A)
        A[j+1] = key                   # insert key where reqd. .. account for -1 above
        if(verbose): print("iter #", i, " :: ", A)
    if(desc): A = A[::-1]
    return(A)
