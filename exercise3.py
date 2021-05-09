import collections
import itertools


alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def decrypt(ciphertext):
    plaintext = ''

    # This will slice the string using a step of 6. The string will be divided into 6 segments
    # i.e: letter 0 -> segment 0, letter 1 -> segment 1 ... l5->s5, l6->s0, l7->s1
    segments = [ciphertext[seg::6] for seg in range(0, 6)]

    # List comprehension is great. This line does the same as the following:
    # counters = list()
    # for segment in segments:                                  For all the items in the list 'segmented'
    #     counters.append(collections.Counter(segment))         Do a frequency analysis
    counters = [collections.Counter(segment) for segment in segments]
    for counter in counters:
        print(counter)

    # The counter output is the following:
    # Counter({'M': 17, 'A': 17, 'I': 15, 'W': 13, 'B': 11, 'P': 9, 'Z': 9, 'Q': 9, 'V': 7, 'G': 5, 'D': 4, 'L': 4, 'J': 3, 'O': 3, 'T': 3, 'U': 3, 'C': 2, 'E': 2, 'K': 2, 'N': 1, 'X': 1})
    # Counter({'P': 18, 'E': 13, 'Y': 13, 'Z': 13, 'L': 11, 'S': 10, 'W': 8, 'T': 8, 'X': 7, 'D': 6, 'C': 5, 'F': 5, 'R': 5, 'O': 4, 'Q': 3, 'H': 2, 'N': 2, 'V': 2, 'J': 2, 'M': 1, 'G': 1, 'A': 1})
    # Counter({'T': 15, 'D': 12, 'P': 12, 'C': 10, 'L': 10, 'X': 10, 'I': 9, 'H': 9, 'J': 8, 'S': 8, 'G': 5, 'A': 5, 'U': 5, 'Q': 4, 'N': 4, 'B': 3, 'V': 3, 'Z': 2, 'R': 2, 'W': 2, 'K': 1, 'E': 1})
    # Counter({'U': 20, 'F': 17, 'P': 13, 'B': 12, 'O': 11, 'J': 9, 'T': 9, 'S': 8, 'M': 5, 'Z': 5, 'I': 5, 'N': 4, 'X': 4, 'G': 4, 'V': 3, 'W': 3, 'E': 2, 'Q': 2, 'D': 2, 'L': 1, 'H': 1})
    # Counter({'I': 14, 'F': 14, 'J': 13, 'P': 11, 'O': 10, 'U': 9, 'S': 9, 'B': 9, 'M': 8, 'T': 7, 'E': 6, 'G': 6, 'X': 5, 'N': 4, 'V': 4, 'D': 3, 'H': 3, 'Z': 3, 'L': 1, 'Q': 1})
    # Counter({'L': 18, 'P': 13, 'H': 12, 'V': 11, 'K': 10, 'Z': 10, 'A': 9, 'U': 7, 'Y': 7, 'F': 7, 'T': 6, 'S': 5, 'B': 5, 'O': 4, 'J': 4, 'R': 3, 'N': 2, 'M': 2, 'I': 2, 'W': 1, 'C': 1, 'D': 1})
    #
    # Given that E is the most common character in the English language we can assume the highest frequency
    # characters are E
    # We can thus calculate the value by which each character is shifted from E
    # In this case we will take the first two characters from each counter i.e. M: 17 and A : 17
    #
    # Index 0 = 8 or -4
    # Index 1 = 11 or 0
    # Index 2 = 15 or -1
    # Index 3 = 16 or 1
    # Index 4 = 4 or 1
    # Index 5 = 7 or 11
    #
    # Initially tested the most common characters, followed by adjustments based on the plaintext results
    # that I got. This lead me to using the shift values of 8, 11, 15, 1, 1, 7

    # Future work need to figure out a way to find all the permutations of the first 2 top results
    # rather than doing the manual work
    '''
    list1 = [counter.most_common(2)[0][0] for counter in counters]
    list2 = [counter.most_common(2)[1][0] for counter in counters]
    list1_permutations = list(itertools.permutations(zip(list1, list2)))

    #for item in list1_permutations:

    #for i in range(len(list1_permutations)):
    #    for j in range(len(list1_permutations[i])):
    #        print(list1_permutations[i][j])

    for col in list1_permutations:
        for row in col:
            print(row)
    '''

    '''
    permutations = list()
    for counter in counters:
        #print(counter.most_common(2))
        permutations.append(list(itertools.permutations(counter.most_common(2))))

    more_perms = list(itertools.permutations(permutations))
    #print(more_perms)

    x = [item[0] for item in more_perms]
    y = [item[0] for item in x]
    for item in y:
        print(item)
    '''

    shift_values = [
        8,
        11,
        15,
        1,
        1,
        7
    ]

    for i in range(len(ciphertext)):
        p = alphabet[alphabet.find(ciphertext[i]) - shift_values[i % 6] % 26]
        plaintext += p

    return plaintext


if __name__ == '__main__':
    # Test cases
    ciphertext = 'PLKFOVBMTFOHJWTUPAPTCLXOIELFDHVODJTOIYIBTRGZJUPSMEBFMPDPLJUOGZJBONMWQFDHCDTJIHDPCPSPOSIUPPASPMMUWELSJAMEDNPAPPGBOKATHUFYAEDTBFEPQFNHZCXFEHATHBJKQHDVMKLZPOEPASPOUMQYXTIAPPVPPKPFHTJMQNJUPBBLCENLIYIUPTIVTXIPTPLFXLZPXOMVLRXOHZASPOUFWFCPJZPLCUEVIYNUIPVRJOMLADNPVVZOTSNLBZPOEPNJDVHVIHPZGYWXBFJZPLAMOVBQDMMVEPTBOKQQNPVUMGTSTWMLZUPTMLCZNVZPXTIHTWCPUHAVLIZBVWTTTFWFIFMSUPXNBFIYSJGPWCSFSFWFIPEVIYNUIPVRXXJSTZQFZFWFAJLLGZJSXYMERIFKAWPWFLDPCJGPBTHUPSQPSPXUIYSEJLGZJBSLDPGZHVWOQVUPBDISJRMDBFUOIEIIFYMTHBXHVEDGIHZXDOZIMELFFUGZJSQYMDTOUTWZSPGZMWUTBJZTUJDLIYSZPBZAPTUTWZSPGZMWUQSLAPGWBAQZCUILAPLFSLBSTGJYAELPSKAZUBOAIRDOJZUEDGMPVRTMBIWCPUFZICRBTTALIUFZASDXFCMCLBTTCNWMJRMQAJONQYVUILULIBEVOZGDBABSTDIHZXHPGAPPXSTBJEAFUFXLHTFKJJWFSBVLEQSLKTPUFKIYSTILWYAZSLKPXWFKBSTNBZQYXNJJIWHPVULDLIJJPXTBOABSPUBUOPGSVSMOHIFYMXPJOLLXJUFUWEZOPDQYVUIHBSTXBZAXDUILZTCHIPALUGFJ'

    pt = decrypt(ciphertext)

    print(pt[0:30])
    print(pt)

    # Essentially a lazy alternative to manually checking for English text from the results
    with open('/Users/saptarshinath/Desktop/tess26.txt') as file:
        contents = file.read()
        if pt in contents:
            print('Match Found')

        print()
