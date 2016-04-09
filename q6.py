import math

def calc_formula(alist):
    c = 50
    h = 30

    blist = [int (math.sqrt ((2 * c * int(d))/h)) for d in alist]

    return blist

if __name__ == '__main__':
    alist = list(raw_input().split(','))
    print calc_formula(alist)
