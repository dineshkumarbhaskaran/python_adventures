
def compare_fun(x, y):
    n1, a1, h1 = x
    n2, a2, h2 = y

    if n1 == n2:
        if int(a1) == int(a2):
            return int(h1) - int(h2)
        else:
            return int(a1) - int(a2)
    else:
        return cmp(n1, n2)

def sort_tuples():
    l = []

    while True:
        s = raw_input()
        if not s:
            break

        t = s.split(',')
        l.append (tuple(t))

    print sorted(l, cmp=compare_fun)

if __name__ == '__main__':
    sort_tuples()
