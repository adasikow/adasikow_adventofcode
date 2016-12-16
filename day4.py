import re
from string import ascii_lowercase
import sys


class IdValidator:

    def __init__(self):
        self.letters_freq = { letter : 0 for letter in ascii_lowercase }
        self.letters_count = len(ascii_lowercase)

    def validate(self, room):
        room_id = ''
        i = 0

        while not room[i].isdigit():
            if room[i] != '-':
                self.letters_freq[room[i]] += 1

            i += 1

        while room[i].isdigit():
            room_id += room[i]
            i += 1

        i += 1
        prop_order = [v[0] for v in sorted(self.letters_freq.iteritems(), key=lambda(k, v): (-v, k))][:5]
        checksum = []
        while room[i] != ']':
            checksum.append(room[i])
            i += 1

        if prop_order == checksum:
            return room_id
        else:
            return None

    def encrypt(self, room):
        room_name = ''
        room_id = ''
        i = len(room) - 1
        while not room[i].isdigit():
            i -= 1

        while room[i].isdigit():
            room_id = room[i] + room_id
            i -= 1

        encrypt_key = long(room_id) % self.letters_count

        for letter in room[:i]:
            if letter == '-':
                room_name += ' '
            else:
                room_name += chr(ord('a') + ((ord(letter) - ord('a') + encrypt_key) % self.letters_count))

        return room_name


def main():
    result = 0
    for line in sys.stdin:
        room_validator = IdValidator()
        room_id = room_validator.validate(line)
        if room_id is not None:
            result += int(room_id)
            room_name = room_validator.encrypt(line)
            print "Room ID: " + room_id + ', room name: ' + room_name

    print "ID sum: " + str(result)


def test(line):
    room_validator = IdValidator()
    room_id = room_validator.validate(line)
    if room_id is not None:
        print "Room ID: " + room_id + ', room name: ' + room_validator.encrypt(line)
    else:
        print "Not a proper room"


if __name__ == '__main__':
    main()
