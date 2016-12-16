import re
import sys


def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a


def main():
    result = 0
    state = 0
    for line in sys.stdin:
        if state == 0:
            a1, a2, a3 = line.split()
            a1, a2, a3 = int(a1), int(a2), int(a3)
        elif state == 1:
            b1, b2, b3 = line.split()
            b1, b2, b3 = int(b1), int(b2), int(b3)
        elif state == 2:
            c1, c2, c3 = line.split()
            c1, c2, c3 = int(c1), int(c2), int(c3)
            if is_triangle(a1, b1, c1):
                result += 1
            if is_triangle(a2, b2, c2):
                result += 1
            if is_triangle(a3, b3, c3):
                result += 1
        state = (state + 1) % 3

    print 'Triangles: ' + str(result)


if __name__ == '__main__':
    main()