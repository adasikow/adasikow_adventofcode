import sys
import re


class Screen:

    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._matrix = [['.' for col in range(self._width)] for row in range(self._height)]

    def _swap(self, row1, col1, row2, col2):
        temp = self._matrix[row1][col1]
        self._matrix[row1][col1] = self._matrix[row2][col2]
        self._matrix[row2][col2] = temp

    def display(self):
        for row in range(self._height):
            line = ''
            for col in range(self._width):
                line += self._matrix[row][col]
            print line

    def number_of_pixels(self):
        result = 0
        for row in range(self._height):
            for col in range(self._width):
                if self._matrix[row][col] == 'x':
                    result += 1
        return result

    def rect(self, a, b):
        for col in range(min(a, self._width)):
            for row in range(min(b, self._height)):
                self._matrix[row][col] = 'x'

    def rotate_column(self, a, b):
        new_col = [None] * self._height
        for row in range(self._height):
            new_col[(row + b) % self._height] = self._matrix[row][a]

        for row in range(self._height):
            self._matrix[row][a] = new_col[row]

    def rotate_row(self, a, b):
        new_row = [None] * self._width
        for col in range(self._width):
            new_row[(col + b) % self._width] = self._matrix[a][col]

        for col in range(self._width):
            self._matrix[a][col] = new_row[col]


def main():
    screen = Screen(50, 6)
    command_rect = 'rect '
    command_rotate_row = 'rotate row y='
    command_rotate_col = 'rotate column x='
    command_regex = r"(" + re.escape(command_rect) + \
                    r"|" + re.escape(command_rotate_row) + \
                    r"|" + re.escape(command_rotate_col) + \
                    r")(\d+)( by |x)(\d+)"
    for line in sys.stdin:
        m = re.match(command_regex, line)
        command = m.group(1)
        a, b = int(m.group(2)), int(m.group(4))
        if command == command_rect:
            screen.rect(a, b)
        elif command == command_rotate_row:
            screen.rotate_row(a, b)
        elif command == command_rotate_col:
            screen.rotate_column(a, b)
        else:
            print "Unknown command"

    screen.display()
    print "Display lit: " + str(screen.number_of_pixels())


def test():
    screen = Screen(7, 3)
    screen.rect(3, 2)
    screen.rotate_column(1, 1)
    screen.rotate_row(0, 4)
    screen.rotate_column(1, 1)
    screen.display()

if __name__ == '__main__':
    main()
