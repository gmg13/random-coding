# code
# howdy!! yeowhhww
import heapq


def main():
    # get the number of cases
    ncases = int(input())
    # initialize low heap, high heap and mid elem
    low = []
    high = []
    mid = None
    # and loop through
    for _ in range(ncases):
        nu = int(input())
        # first the insertion procedure
        if mid is None:
            if not low:
                mid = nu
            else:
                lo = -low[0]
                hi = high[0]
                # check with low .. if yes, then remove small
                # there and insert new elem there
                if nu < lo:
                    lo = -heapq.heapreplace(low, -nu)
                    mid = lo
                # else same to the high side
                elif nu > hi:
                    hi = heapq.heapreplace(high, nu)
                    mid = hi
                else:
                    # keep it as it is
                    mid = nu
        else:
            if nu < mid:
                heapq.heappush(low, -nu)
                heapq.heappush(high, mid)
            else:
                heapq.heappush(low, -mid)
                heapq.heappush(high, nu)
            mid = None

        # then the printing of running median
        if mid:
            print(mid)
        else:
            print(int((high[0] - low[0]) / 2))


if __name__ == '__main__':
    main()
