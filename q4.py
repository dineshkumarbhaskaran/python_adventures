
def create_list_tuple():
    a = list()
    b = tuple ()

    print 'Enter the numbers '
    while True:
        c = int (raw_input())
        if c == -1: 
            break

        a.append (c)
    b = str(a)
    print a 
    print b
        
if __name__ == "__main__":
    create_list_tuple()
