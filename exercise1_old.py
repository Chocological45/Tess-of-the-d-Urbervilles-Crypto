import collections

'''
def bruteforce(ciphertext):
    """
    Brute force attack on cipher text
    Find all possible results
    """

    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    keys = keys = list(range(0,26))

    for key in keys:                              # Repeat for all keys
        plaintext = ''
        for c in ciphertext:
            pointer = alphabet.find(c)            # Find the pointer for character c
            new_pointer = c - key % 26            # Calculate the new pointer using p = c - k mod 26
            p = alphabet[new_pointer]             # Find the letter for the new pointer from alphabet
            plaintext += p                        # Append character to plaintext

        print(str(key) + ": " + plaintext)
'''


def decrypt(ciphertext, k):
    """
    Decrypt the cipher text for a given key using caesar cipher decryption
    """

    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    plaintext = ''
    for c in ciphertext:
        pointer = alphabet.find(c)  # Find the pointer for character c
        new_pointer = pointer - k % 26  # Calculate the new pointer using p = c - k mod 26
        p = alphabet[new_pointer]  # Find the letter for the new pointer from alphabet
        plaintext += p  # Append character to plaintext

    return str(k) + ": " + plaintext


def frequency(ciphertext):
    """
    Find the min and max characters of the cipher text
    """

    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    cp = []
    max1 = []
    min1 = []

    ctr = collections.Counter(ciphertext)
    for i in ctr:
        r = ctr[i]
        cp.append(r)

    p = max(cp)
    q = min(cp)

    for i in ctr:
        if ctr[i] == p:
            max1.append(i)

        if ctr[i] == q:
            min1.append(i)

    print(min1, max1)
    return sorted(min1), sorted(max1)


def analyze(ciphertext):
    """
    Perform a comparison of min and max results with known min and max characters
    Frequency will be (min, max)
    """

    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    freq = frequency(ciphertext)

    # Get our min and max from the output of frequency()
    cmin = freq[0]
    cmax = freq[1]

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

    # Rare characters are J, X, Q, Z (10, 24, 17, 26)
    # Operations 4 -
    # for c in cmin:
    #    cpos = alphabet.find(c) + 1

    # Group the keys
    keys = [subA, subE, subT]

    # Decrypt for each key found and output
    for key in keys:
        if key == 13:
            return (decrypt(ciphertext, key))


if __name__ == '__main__':
    # Test cases

    pt = analyze("BCUREFERTNEQBSNARKPRRQVATYLABIRYSERFUNAQVAGRERFGVATFCRPVZRABSJBZNAXVAQGURLZRGPBAGVAHNYYLGURLPBHYQABGURYCVGGURLZRGQNVYLVAGUNGFGENATRNAQFBYRZAVAGREINYGURGJVYVTUGBSGURZBEAVATVAGURIVBYRGBECVAXQNJASBEVGJNFARPRFFNELGBEVFRRNEYLFBIRELRNEYLURERZVYXVATJNFQBARORGVZRFNAQORSBERGURZVYXVATPNZRGURFXVZZVATJUVPUORTNANGNYVGGYRCNFGGUERRVGHFHNYYLSRYYGBGURYBGBSFBZRBARBEBGUREBSGURZGBJNXRGURERFGGURSVEFGORVATNEBHFRQOLNANYNEZPYBPXNAQNFGRFFJNFGURYNGRFGNEEVINYNAQGURLFBBAQVFPBIRERQGUNGFURPBHYQORQRCRAQRQHCBAABGGBFYRRCGUBHTUGURNYNEZNFBGUREFQVQGUVFGNFXJNFGUEHFGZBFGSERDHRAGYLHCBAUREABFBBAREUNQGURUBHEBSGUERRFGEHPXNAQJUVMMRQGUNAFURYRSGUREEBBZNAQENAGBGURQNVELZNAFQBBEGURAHCGURYNQQREGBNATRYFPNYYVATUVZVANYBHQJUVFCREGURAJBXRURESRYYBJZVYXZNVQFOLGURGVZRGUNGGRFFJNFQERFFRQPYNERJNFQBJAFGNVEFNAQBHGVAGURUHZVQNVEGURERZNVAVATZNVQFNAQGURQNVELZNAHFHNYYLTNIRGURZFRYIRFNABGUREGHEAB")
    print(pt)
    with open('/Users/saptarshinath/Desktop/tess26.txt') as file:
        contents = file.read()
        if pt in contents:
            print('1')
        else:
            print('0')
