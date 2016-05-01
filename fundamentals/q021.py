
import math

def traverse():
    cord = [0, 0]
    while True:
        s = raw_input()
        if s == '':
            break;
        direct, steps = s.split()
        
        if direct == 'UP':
            cord[1] += int(steps)
        if direct == 'DOWN':
            cord[1] -= int(steps)
        if direct == 'LEFT':
            cord[0] -= int(steps)
        if direct == 'RIGHT':
            cord[0] += int(steps)

    print int(math.sqrt(cord[0] * cord[0] + cord[1] * cord[1]))

if __name__ == '__main__':
    traverse()
