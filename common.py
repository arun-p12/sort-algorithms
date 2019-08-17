################################
###  Commonly used routines  ###
################################
def minimum(A):
    try:
        min, index = A[0], 0
        for i in range(1, len(A)):
            if (A[i] < min):
                min = A[i]
                index = i
        return (min, index)
    except:
        print("List expected. Got : ", A)
        exit(1)


def maximum(A):
    try:
        max, index = A[0], 0
        for i in range(1, len(A)):
            if (A[i] > max):
                max = A[i]
                index = i
        return (max, index)
    except:
        print("List expected. Got : ", A)
        exit(1)

def swap(a, b):
    temp = a        # using a temp variable to swap entities not limited to numbers
    a = b
    b = temp
    return(a, b)