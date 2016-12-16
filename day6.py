import operator
import sys


def get_most_freq_char(freq_map):
    return max(freq_map.iteritems(), key=operator.itemgetter(1))[0]


def get_least_freq_char(freq_map):
    return min(freq_map.iteritems(), key=operator.itemgetter(1))[0]


def decode_message(line_len):
    freq_map = [{} for i in range(line_len)]

    print "line_len " + str(line_len)
    for line in sys.stdin:
        for i in range(line_len):
            char = line[i]
            if char not in freq_map[i]:
                freq_map[i][char] = 1
            else:
                freq_map[i][char] += 1

    result = ''
    for i in range(line_len):
        result += get_least_freq_char(freq_map[i])

    return result


def main():
    print decode_message(8)


def test():
    print decode_message(6)

if __name__ == '__main__':
    main()
