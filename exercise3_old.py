import collections


def decrypt(ciphertext):
    plaintext = ''

    key_length = 6
    pos = {
        0: [],
        1: [],
        2: [],
        3: [],
        4: [],
        5: []
    }
    i = 0
    for char in ciphertext:
        pos[i % 6].append(char)
        i += 1

    for n in pos:
        data = collections.Counter(pos[n])
        print('Pos ' + str(n) + ': ' + str(data))

    '''
    Pos 0: Counter({'M': 17, 'A': 17, 'I': 15, 'W': 13, 'B': 11, 'P': 9, 'Z': 9, 'Q': 9, 'V': 7, 'G': 5, 'D': 4, 'L': 4, 'J': 3, 'O': 3, 'T': 3, 'U': 3, 'C': 2, 'E': 2, 'K': 2, 'N': 1, 'X': 1})
    Pos 1: Counter({'P': 18, 'E': 13, 'Y': 13, 'Z': 13, 'L': 11, 'S': 10, 'W': 8, 'T': 8, 'X': 7, 'D': 6, 'C': 5, 'F': 5, 'R': 5, 'O': 4, 'Q': 3, 'H': 2, 'N': 2, 'V': 2, 'J': 2, 'M': 1, 'G': 1, 'A': 1})
    Pos 2: Counter({'T': 15, 'D': 12, 'P': 12, 'C': 10, 'L': 10, 'X': 10, 'I': 9, 'H': 9, 'J': 8, 'S': 8, 'G': 5, 'A': 5, 'U': 5, 'Q': 4, 'N': 4, 'B': 3, 'V': 3, 'Z': 2, 'R': 2, 'W': 2, 'K': 1, 'E': 1})
    Pos 3: Counter({'U': 20, 'F': 17, 'P': 13, 'B': 12, 'O': 11, 'J': 9, 'T': 9, 'S': 8, 'M': 5, 'Z': 5, 'I': 5, 'N': 4, 'X': 4, 'G': 4, 'V': 3, 'W': 3, 'E': 2, 'Q': 2, 'D': 2, 'L': 1, 'H': 1})
    Pos 4: Counter({'I': 14, 'F': 14, 'J': 13, 'P': 11, 'O': 10, 'U': 9, 'S': 9, 'B': 9, 'M': 8, 'T': 7, 'E': 6, 'G': 6, 'X': 5, 'N': 4, 'V': 4, 'D': 3, 'H': 3, 'Z': 3, 'L': 1, 'Q': 1})
    Pos 5: Counter({'L': 18, 'P': 13, 'H': 12, 'V': 11, 'K': 10, 'Z': 10, 'A': 9, 'U': 7, 'Y': 7, 'F': 7, 'T': 6, 'S': 5, 'B': 5, 'O': 4, 'J': 4, 'R': 3, 'N': 2, 'M': 2, 'I': 2, 'W': 1, 'C': 1, 'D': 1})
    
    Assuming the most common letter is E then
    Pos 0 is shifted 8 or -4
    Pos 1 is shifted 11
    Pos 2 is shifted 15
    Pos 3 is shifted 16 (It's actually 1)
    Pos 4 is shifted 4 or 1
    Pos 5 is shifted 7
    
    
    '''
    alphabet = {
        'A': 0,
        'B': 1,
        'C': 2,
        'D': 3,
        'E': 4,
        'F': 5,
        'G': 6,
        'H': 7,
        'I': 8,
        'J': 9,
        'K': 10,
        'L': 11,
        'M': 12,
        'N': 13,
        'O': 14,
        'P': 15,
        'Q': 16,
        'R': 17,
        'S': 18,
        'T': 19,
        'U': 20,
        'V': 21,
        'W': 22,
        'X': 23,
        'Y': 24,
        'Z': 25
    }

    rev_alphabet = {
        0: 'A',
        1: 'B',
        2: 'C',
        3: 'D',
        4: 'E',
        5: 'F',
        6: 'G',
        7: 'H',
        8: 'I',
        9: 'J',
        10: 'K',
        11: 'L',
        12: 'M',
        13: 'N',
        14: 'O',
        15: 'P',
        16: 'Q',
        17: 'R',
        18: 'S',
        19: 'T',
        20: 'U',
        21: 'V',
        22: 'W',
        23: 'X',
        24: 'Y',
        25: 'Z'
    }

    my_chars = []
    for char in ciphertext:
        my_chars.append(alphabet[char])

    shift = {
        0: 8,
        1: 11,
        2: 15,
        3: 1,
        4: 1,
        5: 7
    }

    i = 0
    shifted_chars = []
    for char in my_chars:
        shifted_chars.append(rev_alphabet[(char - shift[i%6])%26])
        i += 1

    plaintext = ''.join(str(x) for x in shifted_chars)

    return plaintext


if __name__ == '__main__':
    # Test cases
    ciphertext = 'PLKFOVBMTFOHJWTUPAPTCLXOIELFDHVODJTOIYIBTRGZJUPSMEBFMPDPLJUOGZJBONMWQFDHCDTJIHDPCPSPOSIUPPASPMMUWELSJAMEDNPAPPGBOKATHUFYAEDTBFEPQFNHZCXFEHATHBJKQHDVMKLZPOEPASPOUMQYXTIAPPVPPKPFHTJMQNJUPBBLCENLIYIUPTIVTXIPTPLFXLZPXOMVLRXOHZASPOUFWFCPJZPLCUEVIYNUIPVRJOMLADNPVVZOTSNLBZPOEPNJDVHVIHPZGYWXBFJZPLAMOVBQDMMVEPTBOKQQNPVUMGTSTWMLZUPTMLCZNVZPXTIHTWCPUHAVLIZBVWTTTFWFIFMSUPXNBFIYSJGPWCSFSFWFIPEVIYNUIPVRXXJSTZQFZFWFAJLLGZJSXYMERIFKAWPWFLDPCJGPBTHUPSQPSPXUIYSEJLGZJBSLDPGZHVWOQVUPBDISJRMDBFUOIEIIFYMTHBXHVEDGIHZXDOZIMELFFUGZJSQYMDTOUTWZSPGZMWUTBJZTUJDLIYSZPBZAPTUTWZSPGZMWUQSLAPGWBAQZCUILAPLFSLBSTGJYAELPSKAZUBOAIRDOJZUEDGMPVRTMBIWCPUFZICRBTTALIUFZASDXFCMCLBTTCNWMJRMQAJONQYVUILULIBEVOZGDBABSTDIHZXHPGAPPXSTBJEAFUFXLHTFKJJWFSBVLEQSLKTPUFKIYSTILWYAZSLKPXWFKBSTNBZQYXNJJIWHPVULDLIJJPXTBOABSPUBUOPGSVSMOHIFYMXPJOLLXJUFUWEZOPDQYVUIHBSTXBZAXDUILZTCHIPALUGFJ'

    pt = decrypt(ciphertext)

    print(pt)

    # Essentially a lazy alternative to manually checking for English text from the results
    with open('/Users/saptarshinath/Desktop/tess26.txt') as file:
        contents = file.read()
        if pt in contents:
            print('Match Found')

        print()
