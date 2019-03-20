class OccursMap:
    def __init__(self):
        self.lookup = {}
        self.size = 0

    def incr(self, ch):
        if ch in self.lookup:
            self.lookup[ch] += 1
        else:
            self.lookup[ch] = 1
        self.size += 1

    def decr(self, ch):
        if self.lookup[ch] == 1:
            del self.lookup[ch]
        else:
            self.lookup[ch] -= 1
        self.size -= 1


def solver(s, k):
    """given a string and a number k, get the length of the longest
    substring that contains at most k distinct elements"""
    # max settings
    maxl = 0
    # window setting
    left = 0
    right = 0
    occurs = OccursMap()

    # main loop
    while right < len(s):
        # increment to the right
        occurs.incr(s[right])
        right += 1

        # check for condition
        while len(occurs.lookup) > k:
            occurs.decr(s[left])
            left += 1

        # and update maxes
        maxl = max(maxl, occurs.size)

    # return the result
    return maxl
