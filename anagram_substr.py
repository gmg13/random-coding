def checksuccess(counter):
    return len(counter) == 0


def updatecounter(left, right, counter):
    # deal with left first
    if left is not None:
        if left in counter:
            if counter[left] == 1:
                counter.pop(left)
            else:
                counter[left] -= 1
        else:
            counter[left] = -1

    # now deal with right
    if right is not None:
        if right in counter:
            if counter[right] == -1:
                counter.pop(right)
            else:
                counter[right] += 1
        else:
            counter[right] = 1


def solver(s, sub):
    # solve for edge case
    if len(s) < len(sub):
        return 0

    # init count map
    counter = {}

    # init total count
    totcount = 0

    # loop through sublist first
    for ch in sub:
        counter.setdefault(ch, 0)
        counter[ch] -= 1

    # let n be the length of string
    # and k be the length of substring to match
    # ... then go through the first k chars in string not
    for i in range(0, len(sub)):
        updatecounter(None, s[i], counter)

    # and now check everytime for a possibility of victory
    # while going right towards edge of earth
    # check first
    # if success, then update found element
    if checksuccess(counter):
        totcount += 1

    left, right = 0, len(sub)
    while right < len(s):
        # update counter
        updatecounter(s[left], s[right], counter)
        # if success, then update found element
        if checksuccess(counter):
            totcount += 1
        # and update the pointers
        left += 1
        right += 1

    return totcount

