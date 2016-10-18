import sys


def draw(ticks, metric):
    if ticks == 0: 
        return

    if ticks == 1:
        print '-'
        return

    draw (ticks - 1, ' ')
    print '-' * ticks, metric
    if metric == ' ':
        draw (ticks - 1, ' ')

if __name__ == '__main__':
    length = int (raw_input('Enter size of the ruler: '))
    ticks  = int (raw_input('Enter tick len: '))

    for i in range(0, length):
        draw(ticks, i + 1)
