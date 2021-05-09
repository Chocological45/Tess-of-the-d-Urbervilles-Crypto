import collections
import itertools

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def decrypt(ciphertext):
    plaintext_list = dict()

    for key_length in range(4, 7):
        # This will slice the string using a step of 6. The string will be divided into 6 segments
        # i.e: letter 0 -> segment 0, letter 1 -> segment 1 ... l5->s5, l6->s0, l7->s1
        segments = [ciphertext[seg::key_length] for seg in range(key_length)]

        # List comprehension is great. This line does the same as the following:
        # counters = list()
        # for segment in segments:                                  For all the items in the list 'segmented'
        #     counters.append(collections.Counter(segment))         Do a frequency analysis
        counters = [collections.Counter(segment) for segment in segments]
        # for counter in counters:
        # print(counter)
        list1 = [counter.most_common()[0][0] for counter in counters]
        list2 = [counter.most_common()[1][0] for counter in counters]

        # print(list1)
        # print(list2)

        '''
        Counter({'K': 14, 'P': 14, 'O': 14, 'S': 13, 'C': 13, 'Y': 12, 'D': 12, 'Z': 12, 'Q': 12, 'T': 11, 'N': 9, 'X': 8, 'G': 7, 'B': 7, 'E': 6, 'U': 6, 'R': 5, 'L': 5, 'H': 5, 'M': 5, 'J': 4, 'F': 4, 'V': 4, 'I': 3, 'A': 3, 'W': 2})
        Counter({'O': 15, 'L': 15, 'M': 14, 'P': 13, 'D': 13, 'Z': 11, 'U': 10, 'S': 10, 'C': 10, 'N': 9, 'E': 9, 'V': 9, 'R': 8, 'B': 8, 'Y': 7, 'A': 6, 'F': 6, 'Q': 5, 'J': 5, 'H': 5, 'X': 5, 'T': 4, 'G': 4, 'K': 4, 'I': 3, 'W': 2})
        Counter({'S': 16, 'D': 15, 'N': 14, 'P': 13, 'Z': 12, 'K': 11, 'C': 10, 'O': 10, 'I': 9, 'Q': 9, 'E': 9, 'G': 9, 'L': 8, 'M': 8, 'T': 7, 'A': 6, 'V': 6, 'B': 6, 'Y': 6, 'J': 5, 'H': 5, 'U': 4, 'X': 4, 'F': 3, 'R': 3, 'W': 2})
        Counter({'Z': 14, 'K': 13, 'L': 12, 'N': 12, 'D': 12, 'G': 11, 'B': 11, 'Q': 11, 'E': 10, 'O': 10, 'F': 9, 'S': 8, 'R': 8, 'U': 7, 'M': 7, 'J': 7, 'Y': 7, 'X': 7, 'P': 6, 'I': 5, 'C': 5, 'A': 5, 'V': 4, 'T': 4, 'H': 4, 'W': 1})
        ['K', 'O', 'S', 'Z']
        ['P', 'L', 'D', 'K']
        Counter({'K': 28, 'U': 20, 'N': 20, 'Z': 13, 'G': 12, 'Y': 12, 'O': 9, 'L': 7, 'J': 7, 'X': 7, 'M': 6, 'C': 5, 'A': 4, 'R': 4, 'I': 3, 'Q': 3, 'B': 2, 'H': 2, 'T': 1, 'W': 1, 'S': 1, 'V': 1})
        Counter({'B': 21, 'E': 18, 'Q': 15, 'L': 15, 'X': 14, 'O': 12, 'P': 11, 'K': 9, 'A': 9, 'F': 9, 'R': 6, 'I': 5, 'C': 5, 'T': 5, 'V': 4, 'Z': 3, 'Y': 2, 'S': 2, 'G': 1, 'D': 1, 'H': 1})
        Counter({'Z': 22, 'O': 15, 'V': 14, 'D': 13, 'N': 13, 'C': 13, 'M': 13, 'I': 12, 'J': 9, 'Y': 7, 'H': 7, 'Q': 6, 'G': 5, 'A': 4, 'W': 3, 'P': 3, 'R': 3, 'B': 2, 'F': 2, 'T': 2})
        Counter({'P': 32, 'L': 16, 'S': 15, 'D': 14, 'E': 13, 'T': 13, 'Y': 11, 'O': 10, 'F': 5, 'J': 5, 'R': 5, 'C': 5, 'N': 3, 'X': 3, 'H': 3, 'M': 3, 'W': 3, 'Q': 3, 'U': 2, 'Z': 2, 'A': 1, 'V': 1})
        Counter({'S': 29, 'D': 24, 'G': 13, 'M': 12, 'C': 10, 'Q': 10, 'Z': 9, 'N': 8, 'B': 7, 'R': 6, 'F': 6, 'H': 6, 'K': 5, 'T': 5, 'U': 5, 'O': 3, 'V': 3, 'E': 3, 'L': 2, 'A': 2})
        ['K', 'B', 'Z', 'P', 'S']
        ['U', 'E', 'O', 'L', 'D']
        Counter({'S': 15, 'P': 10, 'C': 9, 'O': 9, 'K': 8, 'Z': 7, 'L': 7, 'Y': 6, 'T': 6, 'N': 6, 'E': 6, 'R': 6, 'I': 6, 'U': 5, 'G': 4, 'Q': 4, 'D': 4, 'X': 3, 'A': 3, 'B': 3, 'H': 3, 'V': 3, 'M': 2, 'F': 2, 'J': 2, 'W': 1})
        Counter({'L': 14, 'O': 9, 'G': 8, 'E': 8, 'M': 8, 'R': 8, 'S': 7, 'K': 7, 'Z': 6, 'B': 6, 'U': 6, 'Q': 6, 'C': 6, 'D': 5, 'N': 5, 'V': 4, 'P': 4, 'X': 4, 'H': 4, 'F': 4, 'J': 3, 'T': 2, 'Y': 2, 'A': 2, 'I': 1, 'W': 1})
        Counter({'D': 12, 'N': 9, 'S': 9, 'P': 9, 'K': 8, 'Y': 8, 'Z': 7, 'G': 7, 'O': 7, 'T': 7, 'Q': 7, 'X': 6, 'M': 6, 'L': 4, 'J': 4, 'U': 4, 'C': 4, 'B': 4, 'I': 3, 'W': 3, 'E': 3, 'V': 3, 'H': 3, 'A': 2, 'F': 1})
        Counter({'Z': 10, 'P': 10, 'D': 10, 'O': 10, 'N': 9, 'L': 8, 'S': 8, 'M': 7, 'K': 7, 'A': 6, 'U': 6, 'R': 6, 'E': 6, 'B': 5, 'I': 4, 'F': 4, 'G': 4, 'V': 4, 'H': 3, 'Y': 3, 'X': 2, 'Q': 2, 'W': 2, 'J': 2, 'T': 1, 'C': 1})
        Counter({'D': 11, 'Q': 10, 'Z': 10, 'C': 10, 'K': 9, 'P': 8, 'O': 8, 'N': 8, 'E': 6, 'B': 6, 'G': 5, 'S': 5, 'M': 5, 'T': 5, 'A': 4, 'F': 4, 'Y': 4, 'V': 4, 'H': 4, 'X': 3, 'J': 3, 'I': 3, 'L': 2, 'R': 2, 'U': 1})
        Counter({'D': 10, 'Z': 9, 'Y': 9, 'Q': 8, 'C': 8, 'B': 8, 'N': 7, 'J': 7, 'F': 7, 'X': 6, 'M': 6, 'O': 6, 'U': 5, 'E': 5, 'V': 5, 'P': 5, 'L': 5, 'T': 5, 'I': 3, 'G': 3, 'A': 3, 'S': 3, 'K': 3, 'R': 2, 'H': 2})
        ['S', 'L', 'D', 'Z', 'D', 'D']
        ['P', 'O', 'N', 'P', 'Q', 'Z']
        
        Assuming E is the most common letter
        Therefore shift values are:
        key length = 4
            Pos0 = 6 or 11
            Pos1 = 10 or 7
            Pos2 = 14 or -1
            Pos3 = 21 or 6
            
        key length = 5
            Pos0 = 6 or 16
            Pos1 = -3 or 0
            Pos2 = 21 or 10
            Pos3 = 11 or 7
            Pos4 = 14 or -1
            
        key length = 6
            Pos0 = 14 or 11
            Pos1 = 7 or 10
            Pos2 = -1 or 9
            Pos3 = 21 or 11
            Pos4 = -1 or 12
            Pos5 = -1 or 21
            
        '''

        '''
        On first pass, key_length of 5 shows the most promising results.
        On second pass, key shift at index 4 gives the correct output plaintext for key_length = 5
        
        '''

    shift_values = [[
            6,  # 11
            10,  # 7
            14,  # -1
            21],  # 6
        [
            6,  # 16
            -3,  # 0
            21,  # 10
            11,  # 7
            -1],  # -1 (This was originally 14 and was changed to -1 to get the actual key combination)
        [
            14,  # 11
            7,  # 10
            -1,  # 9
            21,  # 11
            -1,  # 12
            -1]]  # 21

    for shift in shift_values:
        plaintext = ''
        for i in range(len(ciphertext)):
            p = alphabet[alphabet.find(ciphertext[i]) - shift[i % len(shift)] % 26]
            plaintext += p

        plaintext_list[len(shift)] = plaintext

    return plaintext_list


if __name__ == '__main__':
    # Test cases
    ciphertext = 'KOZLKUKZNNAIYSDNXQPGGADETTIZDRNBWPFGKOSDYRWUDIQNSDLBGESNXODGKZJFKJPVJMUQCTMMPJEGKAVJOGPNPCGKYTSCXNPUOAZYSZEVEVNXOPUKOCPSNLPRGZEZXDGKOENQBZASUEDXRKIAJDZEZHZYCMLMQXIOZLCZNSOLILSKXNMDLLMPBURGOHZYZEGGQCPQJLPMSYTZCDIEDWCOPCEGGQCPEUOBLUKEZCSNXOSDRLQPCNBMQNXTCLSYEZHZYGPDSGPNSDCXNLMJPHTKKAVEGKOYTRWRDPSGPVEZLLJWHYEITFNQHLQKEVOGKOZLKRVMPBKFQPCNBMYNZBNSDMIVYBKADYSUEDDQULHLMJZJFKJPZPMUQCTMMLATSOQHTFNQWPSNXOSDLLMRZBBCPQHROPUKKDQGKEVOMUQMPBKFQPCOQNSDNXYLRAAYPMKKOSTYFVDSOZOCTYQOSZZEZDTXBGJVURGOEUOBTUKEZCDBBMJLUOITMMXIOMODCEGKTVDSNBNLLKXIOSNRNYDCVZLQYBQPAXLFPSNBRPCJFIRCGVOSDRLQPQYADOMUQMTRKXOXHRHDYFZFHPGGSDYFZEMZTMEOSDCEJWDUCOSHYIVDSCBZVNLQCPHXPJUNAOILSZEZOZOOTMDKKVNBUOYPCYLHPSNFIRNLQCPOUPDEHUKJQFABNERZBNDAKFIRGUKJFQKARTSNXMZNSLASDXLRYVNBIEGKVVCQOSZOCUTIDSGFMDZZYMPZQCVDSZFHPSNBTHDXBNFQVODDDJQJDDKTCLSKCAPBZPCLCHBZYOXLYFBKADYSNBGLQMBFTSIEZYEUOOSD'

    pt_list = decrypt(ciphertext)

    for col, pt in pt_list.items():
        print(pt[0:30])
        print(str(col) + ": " + pt)

        with open('/Users/saptarshinath/Desktop/tess26.txt') as file:
            contents = file.read()
            if pt in contents:
                print('Match Found')

            print()
