# code
# howdy!! yeowhhww


from collections import deque


def nextl(q, arr, n):
    ret = {}

    i = 0

    # go through all elements and remove from stack as you see fit
    for i, elem in enumerate(arr):
        # insert sample into map
        ret[i] = -1
        # now check if this element affects the others
        while q:
            head, j = q.pop()
            if head < elem:
                ret[j] = elem
            else:
                q.append((head, j))
                break
        # now insert this element into stack
        q.append((elem, i))

    # clear the queue
    while q:
        q.pop()

    # print the result
    res = []
    for i in range(n):
        res.append(str(ret[i]))
    print(' '.join(res))
    

def main():
    # get the number of cases
    ncases = int(input())
    gendq = deque()
    # and loop through
    for _ in range(ncases):
        n = int(input())
        arr = [int(i) for i in input().split()]
        nextl(gendq, arr, n)


if __name__ == '__main__':
    main()
