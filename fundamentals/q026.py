
def sqr():
    square = {}

    for i in range(1, 21):
        square[i] = i ** 2

    return square

def print_sqr(square):
    for key, values in square.items():
        print key, values

if __name__ == '__main__':
    d = sqr();
    print_sqr(d)
