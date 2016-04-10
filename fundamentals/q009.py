def convert_strings():
    lines = []
    while True:
        s = raw_input()
        if s:
            lines.append(s.upper())
        else:
            break

    print lines

if __name__ == '__main__':
   convert_strings()
