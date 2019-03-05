def solver(n, steps):
    """ n is the number and steps are the list
    of options that a person could take as a step
    """
    # cache for smaller n
    cache = {}

    # define the recursive function
    def rec(_n):
        # base condition
        if _n == 0:
            return 1
        # try returning from cache
        if _n in cache:
            return cache[_n]
        # totaller
        total = 0
        # o/w add it all up
        for s in steps:
            if s <= _n:
                total += rec(_n - s)
        # put in cache
        cache[_n] = total
        # return
        return total

    # final val
    return rec(n)
