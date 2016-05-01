
def get_freq():
    string = raw_input().split()

    d = {}

    for s in string:
        if s in d.keys():
            d[s] += 1
        else:
            d[s] = 1

    sorted(d)
    for  keys, values in d.items():
        print keys, values

if __name__ == '__main__':
    get_freq()
