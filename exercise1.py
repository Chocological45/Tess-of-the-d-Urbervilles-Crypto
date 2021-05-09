import collections
from itertools import chain

# Global variable for english 26 letter alphabet string
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def decrypt(ciphertext, k):
    plaintext = ''
    for c in ciphertext:
        pointer = alphabet.find(c)  # Find the pointer for character c
        new_pointer = pointer - k % 26  # Calculate the new pointer using p = c - k mod 26
        p = alphabet[new_pointer]  # Find the letter for the new pointer from alphabet
        plaintext += p  # Append character to plaintext

    return plaintext


def frequency_analysis(ciphertext):
    frequencies = list()

    # Frequency analysis on the ciphertext using collections.Counter()
    cipher_frequencies = collections.Counter(ciphertext)

    # Get all the frequencies from the counter object
    for counter in cipher_frequencies:
        frequencies.append(cipher_frequencies[counter])

    rev_dict = {}
    for key, value in cipher_frequencies.items():
        rev_dict.setdefault(value, set()).add(key)

    # Search for duplicates using itertools.chain method
    # Find the highest frequency characters
    fmax = list(chain.from_iterable(
        values for key, values in rev_dict.items()
        if key == max(frequencies))
    )

    # Find the lowest frequency characters
    fmin = list(chain.from_iterable(
        values for key, values in rev_dict.items()
        if key == min(frequencies))
    )

    return sorted(fmin), sorted(fmax)




if __name__ == '__main__':
    # Test cases
    ciphertext = 'BCUREFERTNEQBSNARKPRRQVATYLABIRYSERFUNAQVAGRERFGVATFCRPVZRABSJBZNAXVAQGURLZRGPBAGVAHNYYLGURLPBHYQABGURYCVGGURLZRGQNVYLVAGUNGFGENATRNAQFBYRZAVAGREINYGURGJVYVTUGBSGURZBEAVATVAGURIVBYRGBECVAXQNJASBEVGJNFARPRFFNELGBEVFRRNEYLFBIRELRNEYLURERZVYXVATJNFQBARORGVZRFNAQORSBERGURZVYXVATPNZRGURFXVZZVATJUVPUORTNANGNYVGGYRCNFGGUERRVGHFHNYYLSRYYGBGURYBGBSFBZRBARBEBGUREBSGURZGBJNXRGURERFGGURSVEFGORVATNEBHFRQOLNANYNEZPYBPXNAQNFGRFFJNFGURYNGRFGNEEVINYNAQGURLFBBAQVFPBIRERQGUNGFURPBHYQORQRCRAQRQHCBAABGGBFYRRCGUBHTUGURNYNEZNFBGUREFQVQGUVFGNFXJNFGUEHFGZBFGSERDHRAGYLHCBAUREABFBBAREUNQGURUBHEBSGUERRFGEHPXNAQJUVMMRQGUNAFURYRSGUREEBBZNAQENAGBGURQNVELZNAFQBBEGURAHCGURYNQQREGBNATRYFPNYYVATUVZVANYBHQJUVFCREGURAJBXRURESRYYBJZVYXZNVQFOLGURGVZRGUNGGRFFJNFQERFFRQPYNERJNFQBJAFGNVEFNAQBHGVAGURUHZVQNVEGURERZNVAVATZNVQFNAQGURQNVELZNAHFHNYYLTNIRGURZFRYIRFNABGUREGHEAB'

    chars = frequency_analysis(ciphertext)
    # In the case of our given substring
    cmin = chars[0]     # Minimum characters are: D, K
    cmax = chars[1]     # Maximum characters are: R


    '''
        For this section we have pre determined the cmax and cmin values and will
        carry out operations to find the keys for each possibility manually.
        In this case our cmax will be R:18 and cmin D:4, K:11

        We will also ignore the rare characters for this case as the key here is 13
        for R -> E
        '''

    '''
    # Common characters are E, T, A (5, 20, 1)
    Operations 18 - 1 = 17
               18 - 5 = 13
               18 - 20 = 25
    '''
    for c in cmax:
        cpos = alphabet.find(c) + 1
        subA = cpos - 1
        subE = cpos - 5
        subT = 27 + (cpos - 20)

    # Group the keys
    keys = [subA, subE, subT]

    # Decrypt for each key found and output
    for key in keys:
        pt = decrypt(ciphertext, key)
        print(pt[0:30])
        print(str(key) + ": " + pt)

        # Essentially a lazy alternative to manually checking for English text from the results
        with open('/Users/saptarshinath/Desktop/tess26.txt') as file:
            contents = file.read()
            if pt in contents:
                print('Match Found')

        print()
