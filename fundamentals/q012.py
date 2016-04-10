
def all_even(num):
    while num:
        dig = num % 10
        if dig % 2 == 1:
            return 0
        num = num / 10
    return 1

def get_even(start, end):
    l = []
    for i in range (start, end):
        if all_even(i):
            l.append(i)

    s = [str(i) for i in l]
    print ', '.join (s)
        

if __name__ == '__main__':
    get_even(1000, 3001)
