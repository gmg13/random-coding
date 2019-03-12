# no of encodings as in a word if a is 1, b is 2
# ... z is 26. then 12 could either be ab or l


def solver(s):
    cache = {0: 0, 1: 1}
    # 0 not allowed anywhere
    if '0' in s:
        return 0
    r = _solver(s, cache, len(s))
    return r


def _solver(s, cache, pos):
    "we'll go for a recursive solution"
    # check in cache first
    if pos in cache:
        return cache[pos]
    # get first char
    ch = s[0]
    ch2 = s[1]
    # update cache independently
    if ch == '1' or ch == '2' and ch2 <= '6':
        # there is a possibility of ambiguity here
        cache[pos] = _solver(s[1:], cache, pos - 1) + \
            max(_solver(s[2:], cache, pos - 2), 1)
    else:
        cache[pos] = _solver(s[1:], cache, pos - 1)

    # finally return from cache
    return cache[pos]
