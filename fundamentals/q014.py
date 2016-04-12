
def calc_upper_lower():
    print 'Please enter a string'
    string = raw_input()

    l = u = -0
    for i in range(0, len(string)):
        if string[i].islower():
            l = l + 1
        elif string[i].isupper(): 
            u = u + 1

    print 'Upper == ', u
    print 'lower == ', l

if __name__ == '__main__':
    calc_upper_lower()
