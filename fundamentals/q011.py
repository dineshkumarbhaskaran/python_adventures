
def convert():
    binaries = raw_input().split(',')
    values = []
    for i in binaries:
        if int (i, 2) % 5 == 0:
            values.append(i)


    print ', '.join(values)

if __name__ == '__main__':
    convert()
