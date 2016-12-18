import re
import sys


pattern_pair = r'([a-z])\1'
pattern_abba = r'(a-z)(?!(\1))(\2)(\1)'


def is_aba(text, i):
    result = False

    first_char = text[i]
    try:
        if first_char.isalpha():
            second_char = text[i + 1]
            result = first_char != second_char and text[i + 2] == first_char
    except:
        result = False
    finally:
        return result


def is_abba(text, i):
    result = False

    first_char = text[i]
    try:
        if first_char.isalpha():
            second_char = text[i+1]
            result = first_char != second_char and text[i+2] == second_char and text[i+3] == first_char
    except:
        result = False
    finally:
        return result


def get_all_aba(text):
    result = []
    for i in range(len(text)):
        if is_aba(text, i):
            result.append((text[i], text[i+1]))

    return result


def is_containing_abba(text):
    for i in range(len(text)):
        if is_abba(text, i):
            return True

    return False


def is_supporting_tls(text):
    hypernet_sequences = re.findall(r'\[(\w+)\]', text)
    for hypernet_sequence in hypernet_sequences:
        if is_containing_abba(hypernet_sequence):
            return False

    return is_containing_abba(text)


def is_supporting_ssl(text):
    splitted_text = re.split(r'(\[\w+\])', text)
    abas = []
    babs = []
    for text_chunk in splitted_text:
        if text_chunk[0] == '[':
            babs += get_all_aba(text_chunk[1:-1])
        else:
            abas += get_all_aba(text_chunk)

    for (a, b) in abas:
        if (b, a) in babs:
            return True

    return False


def main():
    result = 0
    for line in sys.stdin:
        if is_supporting_ssl(line):
            result += 1

    print "IPs with SSL support: " + str(result)


def test():
    is_supporting_tls('abba[mnop]qrst')
    is_supporting_tls('abcd[bddb]xyyx')
    is_supporting_tls('aaaa[qwer]tyui')
    is_supporting_tls('ioxxoj[asdfgh]zxcvbn')


def test_2():
    print is_supporting_ssl('aba[bab]xyz')
    print is_supporting_ssl('xyx[xyx]xyx')
    print is_supporting_ssl('aaa[kek]eke')
    print is_supporting_ssl('zazbz[bzb]cdb')

if __name__ == '__main__':
    main()
