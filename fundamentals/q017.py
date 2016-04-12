
def compute_net():
    net = 0

    while True:
        s = raw_input()
        if not s:
            break

        c, m = s.split()
        if c == 'D':
            net = net + int (m)
        else:
            net = net - int(m)

    print 'net is = ', net

if __name__ == '__main__':
    compute_net()
