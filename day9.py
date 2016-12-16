import re
import sys


class Decompressor:

    def __init__(self):
        self.re_marker = r'\((\d+)x(\d+)\)'
        self.m = None

    def next_match(self, text):
        self.m = re.search(self.re_marker, text)
        return self.m is not None

    def decompressed_size(self, line):
        current_len = long(0)
        start = long(0)

        while start < len(line) and self.next_match(line[start:]):
            seq_len, repeats = long(self.m.group(1)), long(self.m.group(2))
            marker_start, marker_end = long(self.m.start(0)), long(self.m.end(0))
            current_len += marker_start + (seq_len * repeats)
            start += marker_end + seq_len

        return current_len + len(line[start:])

    def decompressed_size_rec(self, text):
        m = re.search(self.re_marker, text)
        if m is None:
            return len(text)
        else:
            seq_len, repeats = long(m.group(1)), long(m.group(2))
            marker_start, marker_end = long(m.start(0)), long(m.end(0))
            return marker_start + \
                   (self.decompressed_size_rec(text[marker_end:marker_end + seq_len]) * repeats) + \
                   self.decompressed_size_rec(text[marker_end + seq_len:])


def main():
    decompressor = Decompressor()
    result = 0
    for line in sys.stdin:
        line_len = decompressor.decompressed_size(line.strip())
        result += line_len
        print "line len: " + str(line_len)

    print "Len: " + str(result)


def main_2():
    decompressor = Decompressor()
    result = 0
    for line in sys.stdin:
        line_len = decompressor.decompressed_size_rec(line.strip())
        result += line_len
        print "line len: " + str(line_len)

    print "Len: " + str(result)


def test():
    decompressor = Decompressor()
    print 'len: ' + str(decompressor.decompressed_size('ADVENT'))
    print 'len: ' + str(decompressor.decompressed_size('A(1x5)BC'))
    print 'len: ' + str(decompressor.decompressed_size('(3x3)XYZ'))
    print 'len: ' + str(decompressor.decompressed_size('A(2x2)BCD(2x2)EFG'))
    print 'len: ' + str(decompressor.decompressed_size('(6x1)(1x3)A'))
    print 'len: ' + str(decompressor.decompressed_size('X(8x2)(3x3)ABCY'))
    print 'len: ' + str(decompressor.decompressed_size('X(8x2)(3x3)AB(2x2)CY'))


def test_rec():
    decompressor = Decompressor()
    print 'len: ' + str(decompressor.decompressed_size_rec('(3x3)XYZ'))
    print 'len: ' + str(decompressor.decompressed_size_rec('X(8x2)(3x3)ABCY'))
    print 'len: ' + str(decompressor.decompressed_size_rec('(27x12)(20x12)(13x14)(7x10)(1x12)A'))
    print 'len: ' + str(decompressor.decompressed_size_rec('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN'))


if __name__ == '__main__':
    main_2()
