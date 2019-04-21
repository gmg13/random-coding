# code
# howdy!! yeowhhww


def _maxsubarr(n, arr):
    # initiate the cache and max len
    cache = {}
    maxlen = 0
    lastsum = 0
    # loop da loop
    for ix, i in enumerate(arr):
        # renew the last sum
        lastsum += i
        # if lastsum is 0, then this means sum from 0 is 0
        if not lastsum:
            maxlen = max(maxlen, ix + 1)
        # check if it exists already
        # if so, then update max subarr size
        # else, put in cache sigma(0, ix-1)[arr[i]]
        if lastsum in cache:
            maxlen = max(maxlen, ix - cache[lastsum])
        else:
            cache[lastsum] = ix
    return maxlen


def _maxsubarr_brute(n, arr):
    maxlen = 0
    for i in range(n):
        for j in range(i+1, n+1):
            s = sum(arr[i:j])
            if not s:
                maxlen = max(maxlen, j-i)
    return maxlen


def main():
    # get the number of cases
    ncases = int(input())
    # and loop through
    for _ in range(ncases):
        # the total size
        n = int(input())
        # the actual array
        arr = [int(i) for i in input().split()]
        # compute the max len
        maxlen = _maxsubarr_brute(n, arr)
        print(maxlen)


if __name__ == '__main__':
    main()
