# code
# howdy!! yeowhhww


def isbalanced(s):
    # stack of parenthesis
    st = []
    # and loop through the string
    for ch in s:
        if ch in ['{', '[', '(']:
            st.append(ch)
        elif ch == '}':
            if not st:
                print('unbalanced')
                return
            popped = st.pop()
            if popped != '{':
                print('unbalanced')
                return
        elif ch == ']':
            if not st:
                print('unbalanced')
                return
            popped = st.pop()
            if popped != '[':
                print('unbalanced')
                return
        elif ch == ')':
            if not st:
                print('unbalanced')
                return
            popped = st.pop()
            if popped != '(':
                print('unbalanced')
                return
    # done through all
    if not st:
        print('balanced')
    else:
        print('unbalanced')


def main():
    # get the number of cases
    ncases = int(input())
    # and loop through
    for _ in range(ncases):
        s = input()
        isbalanced(s)


if __name__ == '__main__':
    main()
