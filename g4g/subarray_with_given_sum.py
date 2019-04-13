# code
# howdy!! yeowhhww


def subsum(arr, n, expected):
    if expected <= 0 or not arr:
        print('-1')
        return
    # pointers etc.
    lt = 0
    rt = 0
    total = arr[0]

    # go through the loop
    while rt < n and lt < n:
        if total > expected:
            total -= arr[lt]
            lt += 1
        elif total < expected:
            rt += 1
            if rt == n:
                print('-1')
                return
            total += arr[rt]
        else:
            print('%d %d' % (lt + 1, rt + 1))
            return
    # nothing to show for .. so print -1
    print('-1')


def main():
    # get the number of cases
    ncases = int(input())
    # and loop through
    for _ in range(ncases):
        n, s = [int(i) for i in input().split()]
        arr = [int(i) for i in input().split()][:n]
        # and run the algorithm
        subsum(arr, n, s)


if __name__ == '__main__':
    main()
