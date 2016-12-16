import re
import sys


class Keypad:

    def __init__(self):
        self.current_pos = (1,1)
        self.pad = [[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]]

    def up(self):
        self.current_pos = (max(self.current_pos[0] - 1, 0), self.current_pos[1])

    def down(self):
        self.current_pos = (min(self.current_pos[0] + 1, 2), self.current_pos[1])

    def left(self):
        self.current_pos = (self.current_pos[0], max(self.current_pos[1] - 1, 0))

    def right(self):
        self.current_pos = (self.current_pos[0], min(self.current_pos[1] + 1, 2))

    def get_number(self):
        return self.pad[self.current_pos[0]][self.current_pos[1]]

    def get_number_from_commands(self, commands):
        for i in range(len(commands)):
            if commands[i] == 'U':
                self.up()
            elif commands[i] == 'D':
                self.down()
            elif commands[i] == 'L':
                self.left()
            elif commands[i] == 'R':
                self.right()
            else:
                print "Unknown command " + commands[i]

        return str(self.get_number())


class KeypadImproved:

    def __init__(self):
        self.current_pos = (2, 0)
        self.pad = [[' ', ' ', '1', ' ', ' '],
                    [' ', '2', '3', '4', ' '],
                    ['5', '6', '7', '8', '9'],
                    [' ', 'A', 'B', 'C', ' '],
                    [' ', ' ', 'D', ' ', ' ']]

    def up(self):
        old = self.current_pos
        self.current_pos = (max(self.current_pos[0] - 1, 0), self.current_pos[1])
        if self.get_number() == ' ':
            self.current_pos = old

    def down(self):
        old = self.current_pos
        self.current_pos = (min(self.current_pos[0] + 1, 4), self.current_pos[1])
        if self.get_number() == ' ':
            self.current_pos = old

    def left(self):
        old = self.current_pos
        self.current_pos = (self.current_pos[0], max(self.current_pos[1] - 1, 0))
        if self.get_number() == ' ':
            self.current_pos = old

    def right(self):
        old = self.current_pos
        self.current_pos = (self.current_pos[0], min(self.current_pos[1] + 1, 4))
        if self.get_number() == ' ':
            self.current_pos = old

    def get_number(self):
        return self.pad[self.current_pos[0]][self.current_pos[1]]

    def get_number_from_commands(self, commands):
        for i in range(len(commands)):
            if commands[i] == 'U':
                self.up()
            elif commands[i] == 'D':
                self.down()
            elif commands[i] == 'L':
                self.left()
            elif commands[i] == 'R':
                self.right()
            else:
                print "Unknown command " + commands[i]

        return str(self.get_number())


def main():
    keypad = KeypadImproved()
    result = ''
    for line in sys.stdin:
        result += keypad.get_number_from_commands(line.strip())

    print 'Bathroom code: ' + result

if __name__ == '__main__':
    main()