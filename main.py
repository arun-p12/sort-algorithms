##########################
### The main function  ###
##########################

def main():
    def step_thru_code():
        import argparse

        verbose, desc = 0, 0
        text = 'Control program for the various sort algorithms'
        # initiate the parser
        parser = argparse.ArgumentParser()
        parser.add_argument("-v", "--verbose",
                            help='activate verbose print statements [1 | 2]')
        parser.add_argument("-d", "--descending", action='store_true',
                            help='sort in descending order')
        args = parser.parse_args()
        if args.verbose:
            if(args.verbose in ['1', '2']): verbose = int(args.verbose)
        if args.descending: desc = 1
        return(verbose, desc)

    # list of sort algorithms saved independently
    import bubble_sort as b
    import counting_sort as c
    import heap_sort as h
    import insertion_sort as i
    import merge_sort as m
    import radix_sort as r
    import selection_sort as s
    import selection_insertion_sort as si
    import shell_sort as sh
    import quick_sort as q

    '''
    boring stuff: list to sort, capturing verbosity level, and setting a timer
    '''
    import time     # get a sense of the time taken
    A = [3, 14, 27, 12, 31, -6, 945643, 95, 0, 18, 5, 3, 980]
    verbose, desc = step_thru_code()
    print("unsorted   = ", A)
    t = time.time()         # get time just before the main routine


    ######## tweak code / options below  ###########

    #A = b.bubble_sort(A, verbose, desc)
    #A = c.counting_sort(A, verbose, desc)
    #A = h.heap_sort(A, verbose, desc)
    #A = i.insertion_sort(A, verbose, desc)
    #A = m.merge_sort(A, verbose, desc)
    #A = r.radix_sort(A, verbose, desc)
    #A = s.selection_sort(A, verbose, desc)
    #A = si.selection_insertion_sort(A, verbose, desc)
    #A = sh.shell_sort(A, verbose, desc)
    A = q.quick_sort(A, verbose, desc)

    ########## end of modifiable section ###########

    '''
    more boring stuff: stop the timer, print the output result, and the time taken
    '''
    t = time.time() - t             # and now, after the routine
    print("sorted     = ", A)       # we want to see the output, don't we!?
    print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t*1000, t*1000000))


if __name__ == "__main__":
    main()