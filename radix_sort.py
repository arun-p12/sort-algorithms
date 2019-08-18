'''
Also known as Bucket Sort
Radix sort -- time taken as a function of size, and number of digits
    ==> O(d (n + b)), where b is the base ... 10 for numbers, 26 for alphabets etc.

Find the largest number and then the number of digits in it. Iterating thru that many times
would result in a sorted list.  In each iteration:
   - find the 'i'th value of the every number in the list
    - (e.g. for 1st run, unit digit, for second run the 10s digit, etc
    - place the number in a 'bucket' marked by the position value  [[ for base 10 ... 0 to 9 ]]
    - generate updated list sequentially reading from bucket 0 thru bucket 9.
'''


def radix_sort(A, verbose=0, desc=0):
    import common as c
    # calculate the number of passes :: highest order place value
    def passes(n, b):
        cnt = 0
        while (n):
            cnt += 1
            n = n // b
        return (cnt)

    # the digit at the 'pos'th position. e.g. in 3011472 ... 4 is in the 2nd position
    def positional_digit(n, pos, b=10):
        cnt, rem, ok = 0, 0, True  # rem initialized, in case n=0
        while (ok):
            cnt += 1
            rem = n % b
            n = n // b
            if (cnt > pos): ok = False
        return (rem)

    # map all number to their appropriate buckets
    def bucketize(pos, b):
        n = len(A)
        B = [[] for i in range(n)]
        for i in range(n):
            bucket = positional_digit(A[i], pos, b)
            B[bucket].append(A[i])
            if(verbose == 2): print("    B:", i, " :: ", B)
        return ([B[x][y] for x in range(len(B)) for y in range(len(B[x]))])

    # main routine
    b = 10
    smallest = c.minimum(A)[0]
    if(smallest): A = [x - smallest for x in A]     # normalize smallest to 0

    largest = c.maximum(A)[0]  # get the largest number
    iter = passes(largest, b)  # calculate the number of iterations

    for i in range(iter):
        A = bucketize(i, b)  # bucketize for each iteration
        if(verbose): print("iter #", i, " :: ", A)

    if (smallest): A = [x + smallest for x in A]  # undo the normalization
    if(desc): A = A[::-1]
    return (A)
