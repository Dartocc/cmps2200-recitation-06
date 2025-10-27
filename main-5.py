def fib_recursive(n, counts):
    """
    Return the nth Fibonacci number. 
    counts is a list of n+1 elements, where counts[i] is incremented
    each time fib_recursive(i, counts) is called.
    """    
    counts[n] += 1
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Recursive calls
    return fib_recursive(n - 1, counts) + fib_recursive(n - 2, counts)
    

    
def fib_top_down(n, fibs):
    # If already computed, just return it
    if fibs[n] != -1:
        return fibs[n]

    # Base cases
    if n == 0:
        fibs[n] = 0
    elif n == 1:
        fibs[n] = 1
    else:
        fibs[n] = fib_top_down(n - 1, fibs) + fib_top_down(n - 2, fibs)

    return fibs[n]
    



def fib_bottom_up(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    fibs = [0] * (n + 1)
    fibs[1] = 1

    # Build up from smallest to largest
    for i in range(2, n + 1):
        fibs[i] = fibs[i - 1] + fibs[i - 2]

    return fibs[n]

def test_fib_bottom_up():
    n = 10
    print(fib_bottom_up(n))  # should print 55



