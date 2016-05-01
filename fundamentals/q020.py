
def gen_mult7(start = 1):
    while True:
        yield (7 * start)
        start = start + 1


def print_mult7():
    for i in gen_mult7(2):
        if i > 100:
            break;
        print i

if __name__ == '__main__':
    print_mult7()
