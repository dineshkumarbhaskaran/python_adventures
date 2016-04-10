
def ssort(alist):
    alist.sort()
    print alist

if __name__ == '__main__':
    print 'Enter the strings: '
    alist = list (raw_input().split(','))
    ssort(alist)
