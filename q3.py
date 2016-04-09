

def build_dict(num):
    sdict = dict()

    for i in range (1, num + 1):
        sdict[i] = i * i

    print sdict
    return sdict

if __name__ == "__main__":
    sdict = build_dict(8)
    print sdict
