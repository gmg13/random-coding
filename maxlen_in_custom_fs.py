import functools


def baselen(base):
    chlen = functools.reduce(lambda x, y: x + y[1], base, 0)
    return chlen + len(base) - 1


def solver(s):
    """
    dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext is a filesystem string

    find the largest length of any path
    """
    word = []
    base = []
    tabcounter = 0
    inword = False
    # max initialization
    maxch = 0
    for ch in s:
        # consider the odd ones first
        if ch == '\n':
            base.append((''.join(word), len(word)))
            word.clear()
            # compare with max
            maxch = max(baselen(base), maxch)
            # unset inword
            inword = False
        elif ch == '\t':
            tabcounter += 1
        else:
            if not inword:
                base = base[:tabcounter]
                # reset the counter
                tabcounter = 0
                # set inword
                inword = True
            # start adding to the word
            word.append(ch)

    # get last max
    base.append((''.join(word), len(word)))
    # compare with max
    maxch = max(baselen(base), maxch)

    # return the character length of the largest path
    return maxch
