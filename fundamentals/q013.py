
def calc_alnum():
    s = raw_input()
    
    num = 0
    letters = 0

    for i in range(0, len(s)):
        if s[i].isdigit():
            num += 1 
        elif s[i].isalpha():
            letters += 1

    print num, letters


if __name__ == '__main__':
    calc_alnum()
