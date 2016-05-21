''' The problem is to find two number which are closest to each other in a 
    list'''

from random import randrange

def close_abs1(seq):
    diff = float("inf")
    xx, yy = 0, 0
    for x in range(len(seq)):
        for y in range(len(seq)):
            if x == y: continue

            if abs(seq[x] - seq[y]) < diff:
                diff = abs(seq[x] - seq[y])
                xx, yy = seq[x], seq[y]

    print xx, yy


def close_abs(nseq):
    diff = float("inf")
    xx, yy = 0, 0

    ii = 0
    seq = sorted(nseq)
    for i in range(len(seq)-1):
        if abs(seq[i] - seq[i+1]) < diff:
            xx, yy = seq[i], seq[i+1]
            diff = abs(seq[i] - seq[i+1])

    print xx, yy

if __name__ == '__main__':
    seq = [randrange(1000) for i in xrange(15)]
    close_abs(seq)
    close_abs1(seq)
