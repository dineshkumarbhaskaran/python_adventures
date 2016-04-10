#!/usr/bin/python

def check_divisors_7_not_5(start, end):
    l = []
    for i in range(start, end + 1):
        if (i % 7 == 0) and (i % 5 != 0): 
            l.append(str(i))

    return l

if __name__ == "__main__":
    dlist = check_divisors_7_not_5(2000, 3200)   
    print ','.join (dlist)
