import sys
import re


class SantaMap:

    START_POS = (0, 0)

    def __init__(self):
        self.santa_pos = self.START_POS
        self.bunny_pos = None
        self.santa_dir = (0, 1)
        self.visited = set(self.santa_pos)

    def rotate_left(self):
        self.santa_dir = (-1 * self.santa_dir[1], self.santa_dir[0])

    def rotate_right(self):
        self.santa_dir = (self.santa_dir[1], -1 * self.santa_dir[0])

    def move(self, dist):
        for i in range(dist):
            self.santa_pos = (self.santa_pos[0] + self.santa_dir[0], self.santa_pos[1] + self.santa_dir[1])
            if self.santa_pos in self.visited and self.bunny_pos is None:
                self.bunny_pos = self.santa_pos
            self.visited.add(self.santa_pos)

    @staticmethod
    def get_distance(start, target):
        return abs(target[0] - start[0]) + abs(target[1] - start[1])

    def santa_left(self, dist):
        self.rotate_left()
        self.move(dist)

    def santa_right(self, dist):
        self.rotate_right()
        self.move(dist)

    def move_santa(self, cmd_list):
        for cmd in cmd_list:
            cmd = cmd.strip()
            rot = cmd[0].upper()
            dist = int(cmd[1:])
            if rot == 'R':
                self.santa_right(dist)
            elif rot == 'L':
                self.santa_left(dist)
            else:
                print 'unknown command ' + cmd


def main():
    for line in sys.stdin:
        santa_map = SantaMap()
        santa_map.move_santa(line.split(','))
        print 'distance from start to current santa pos: ' + \
              str(santa_map.get_distance(santa_map.START_POS, santa_map.santa_pos))

        if santa_map.bunny_pos:
            print 'distance from start to bunny pos: ' + \
              str(santa_map.get_distance(santa_map.START_POS, santa_map.bunny_pos))


if __name__ == '__main__':
    main()
