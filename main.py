##########################
### The main function  ###
##########################

def main():
    def step_thru_code():
        import argparse

        verbose, asc = False, True
        text = 'Some helper message about the program'
        # initiate the parser
        parser = argparse.ArgumentParser()
        parser.add_argument("-v", "--verbose", action='store_true',
                            help='activate verbose print statements')
        parser.add_argument("-d", "--descending", action='store_true',
                            help='sort in descending order')
        args = parser.parse_args()
        if args.verbose: verbose = True
        if args.descending: asc = False
        return(verbose, asc)

    # list of sort algorithms saved independently
    import bubble_sort as b

    '''
    boring stuff list to sort, capturing verbosity level, and setting a timer
    '''
    import time     # get a sense of the time taken
    A = [3, 14, 27, 12, 31, -6, 945643, 95, 0, 18, 5, 3, 980]
    verbose, asc = step_thru_code()
    print("unsorted   = ", A)
    t = time.time()         # get time just before the main routine


    ######## tweak code / options below  ###########
    A = b.bubble_sort(A, verbose, asc)


    ########## end of modifiable section ###########

    '''
    more boring stuff about recording the time, printing the output result, and the time taken
    '''
    t = time.time() - t             # and now, after the routine
    print("sorted     = ", A)       # we want to see the output, don't we!?
    print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t*1000, t*1000000))


if __name__ == "__main__":
    main()