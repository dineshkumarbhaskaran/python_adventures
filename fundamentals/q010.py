
def wsort():
    words = raw_input().split()
    words = sorted (set (words))
    print ' '.join (words)

if __name__ == '__main__':
    wsort()
