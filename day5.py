import hashlib


class DoorPasswordCracker:

    def __init__(self):
        self.md5 = hashlib.md5()
        self.index = 0

    @staticmethod
    def is_indicating_next_char(door_hash):
        return door_hash[:5] == '00000'

    @staticmethod
    def is_proper_candidate(door_hash):
        return door_hash[:5] == '00000' and door_hash[5].isdigit() and int(door_hash[5]) < 8

    def get_hash(self):
        m = self.md5.copy()
        m.update(str(self.index))
        return m.hexdigest()

    def get_next_char(self):
        while not self.is_indicating_next_char(self.get_hash()):
            self.index += 1

        return self.get_hash()[5]

    def get_next_candidate(self):
        while not self.is_proper_candidate(self.get_hash()):
            self.index += 1

        door_hash = self.get_hash()
        return int(door_hash[5]), door_hash[6]

    def get_password(self, door_id):
        result = 'xxxxxxxx'
        self.md5.update(door_id)

        while 'x' in result:
            pos, char = self.get_next_candidate()
            if result[pos] == 'x':
                char_list = list(result)
                char_list[pos] = char
                result = ''.join(char_list)
            self.index += 1

        return result


def main():
    password_cracker = DoorPasswordCracker()
    print "Door password: " + password_cracker.get_password("abc")

    password_cracker = DoorPasswordCracker()
    print "Door password: " + password_cracker.get_password("cxdnnyjw")


if __name__ == '__main__':
    main()
