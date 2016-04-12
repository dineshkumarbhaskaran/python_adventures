
def check_criterion(password):
    length = len(password)
    if length < 6:
        return False
    if length > 12:
        return False

    l = 0
    u = 0
    s = 0

    for i in range(0, length):
        if password[i].islower():
            l += 1
        if password[i].isupper():
            u += 1
        if password[i] in "$#@":
            s += 1

    print l, u, s
    return l and u and s

def check_password():
    plist = raw_input().split(',')

    for password in plist:
        if check_criterion(password):
            print password

if __name__ == '__main__':
    check_password()
