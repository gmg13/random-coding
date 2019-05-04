# code
# howdy!! yeowhhww


def main():
    # get the number of cases
    ncases = int(input())
    # and loop through
    for _ in range(ncases):
        # get the length, although this is not imp
        input()
        # get the start times first
        st = [int(i) for i in input().split()]
        # and get the end times
        et = [int(i) for i in input().split()]
        # and zip them together before sorting them
        acts = [(i, j) for i, j in zip(st, et)]
        # and sort them of course
        acts.sort(key=lambda x: x[1])
        # set the last set ones and loop through the remaining ones
        laste = -1
        total = 0
        # now choose the next one
        for s, e in acts:
            if s < laste:
                continue
            total += 1
            laste = e
        # and print the total
        print(total)


if __name__ == '__main__':
    main()
