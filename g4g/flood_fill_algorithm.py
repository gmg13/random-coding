# code
# howdy!! yeowhhww


def getix(n, x, y):
    return n * x + y


def draw(prefix, arr, m, n, x, y, K):
    print('-'*(3*n+1))
    print(prefix, x, y, K)
    print('-'*(3*n+1))
    for i in range(m):
        suff = ' '.join(['{:2d}'.format(i) for i in arr[i*n:i*n+n]])
        print(f'|{suff}|')
    print('-'*(3*n+1))


def floodfill(arr, m, n, x, y, prevc, nextc, done):
    # get the index
    i = getix(n, x, y)
    # base condition
    if x < 0 or x >= m or y >= n or y < 0 or i in done:
        return
    # check if current elem is eq to elem
    currc = arr[i]
    # compare if continuable
    if currc == prevc:
        # switch current color
        arr[i] = nextc
        # set the done vector
        done.add(i)
        # and now check right
        floodfill(arr, m, n, x, y+1, prevc, nextc, done)
        # check right
        floodfill(arr, m, n, x, y-1, prevc, nextc, done)
        # check down
        floodfill(arr, m, n, x+1, y, prevc, nextc, done)
        # and check up
        floodfill(arr, m, n, x-1, y, prevc, nextc, done)


def main():
    # get the number of cases
    ncases = int(input())
    # and loop through
    for _ in range(ncases):
        # the total size
        m, n = [int(i) for i in input().split()]
        # the actual array
        arr = [int(i) for i in input().split()]
        # position
        x, y, K = [int(i) for i in input().split()]
        # print the arr
        draw('bef', arr, m, n, x, y, K)
        # initiate the done cache
        done = set()
        # now go fish
        floodfill(arr, m, n, x, y, arr[getix(n, x, y)], K, done)
        draw('aft', arr, m, n, x, y, K)
        # and print the result
        print(*arr)


if __name__ == '__main__':
    main()
