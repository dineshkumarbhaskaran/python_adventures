
def create_array(x, y):
    blist = []
    for i in range(0, y):
        alist = [i * j for j in range(0, x)]
        blist.append (alist)

    print blist

if __name__ == '__main__':
    print 'Enter x, y: '
    alist = list (raw_input().split(','))
    create_array(int(alist[0]), int(alist[1]))
