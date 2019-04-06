def sol(li):
    ret = []
    last = 0
    for e in li:
        last = (last * 2 + e) % 10
        ret.append(not last % 5)
    return ret
