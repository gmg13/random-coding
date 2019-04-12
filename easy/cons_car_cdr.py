def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

# what will be the implementation of car and cdr
# car(cons(3, 4)) => 3
# cdr(cons(3, 4)) => 4
# cons returns a functions which is called on its attrs


def car(l):
    return l(lambda x, y: x)


def cdr(l):
    return l(lambda x, y: y)


def test():
    a = cons(3, 4)
    print(car(a))
