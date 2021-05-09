import collections
import re


def replace(char, substitution):
    substrings = sorted(substitution, key=len, reverse=True)
    regex = re.compile('|'.join(map(re.escape, substrings)))
    return regex.sub(lambda match: substitution[match.group(0)], char)


def decrypt(ciphertext):
    plaintext = ''

    # Frequency analysis of the ciphertext as characters
    frequency_analysis = collections.Counter(ciphertext).most_common()
    #print(frequency_analysis)

    '''
    [('W', 4), ('A', 4), ('L', 5), ('Z', 9), ('R', 9), ('M', 12), ('|', 13), ('T', 13), ('Q', 13), 
    ('G', 14), ('F', 16), ('J', 19), ('O', 26), ('P', 27), ('K', 40), ('Y', 41), ('B', 43), ('N', 48), 
    ('H', 54), ('I', 54), ('V', 62), ('C', 70), ('S', 91), ('D', 153)]
    
    It's safe to assume that | is not whitespace
    
    D is clearly |
    S is likely E
    C is likely T
    V is likely A
    
    [('SVC', 1), ('CHNILSPK', 1), ('SVPISKCOM', 1), ('VZZSVO', 1), ('GVI', 1), ('GSI', 1), ('VKL', 1), ('CSOO', 1), ('HNG', 1), ('CHSNP', 1), ('GSCHBY', 1), ('GBBY', 1), ('CPVIKG|CSY', 1), ('NCKSOF', 1), ('NICB', 1), ('YBRRSY', 1), ('NIYNFFSPSITS', 1), ('CNOO', 1), ('VC', 1), ('OSIRCH', 1), ('FVITNSY', 1), ('OBBLNIR', 1), ('BI', 1), ('BJI', 1), ('SWNKCSITS', 1), ('JNCH', 1), ('ZVKKNAS', 1), ('NICSPSKC', 1), ('VI', 1), ('B|CKNYSP', 1), ('SGQNCCSPSY', 1), ('TBIANTCNBI', 1), ('VOO', 1), ('YSKBOVCNBI', 1), ('QSSI', 1), ('QPB|RHC', 1), ('VQB|C', 1), ('VTTNYSIC', 1), ('QSNIR', 1), ('Y|PQSPANOOS', 1), ('JHSI', 1), ('FB|IY', 1), ('CSKK', 1), ('TVGS', 1), ('SWHV|KCSY', 1), ('VITNSIC', 1), ('ONIS', 1), ('ISJ', 1), ('CPNQSK', 1), ('FPBG', 1), ('QSOBJ', 1), ('FBIYOM', 1), ('YPSVGSY', 1), ('JHM', 1), ('KCBNTVOOM', 1), ('VQVIYBISY', 1), ('NI', 1), ('FNYSONCM', 1), ('ZPNITNZOSK', 1), ('JHVC', 1), ('RBC', 1), ('VZBKCVKM', 1), ('Z|INKHGSIC', 1), ('YSKSPASY', 1), ('CHSI', 1), ('QSTVGS', 1), ('JSVPM', 1), ('VIWNB|K', 1), ('VIWNSCM', 1), ('NITPSVKSY', 1), ('JBIYSPSY', 1), ('NF', 1), ('CPSVCSY', 1), ('|IFVNPOM', 1), ('LIBJNIR', 1), ('YPVIL', 1), ('CVKCNIR', 1), ('HB|PK', 1), ('YPBZZSY', 1), ('', 1), ('CHSG', 2), ('FSOOBJ', 2), ('V', 2), ('CHNK', 2), ('IBC', 2), ('VCS', 2), ('JNCHB|C', 2), ('VK', 3), ('QM', 3), ('HSP', 3), ('CB', 4), ('BF', 4), ('CHVC', 4), ('HNK', 5), ('JVK', 5), ('CHS', 5), ('HVY', 5), ('VIY', 7), ('HS', 12)]

    CHS repeats 5 times, probably THE
    ZZ = x2
    OO = x6 probably LL (This one is useful, the rest are not)
    BB = x2
    RR = x1
    FF = x1
    KK = x2
    CC = x1
    SS = x2
    TT = x1
    
    CHS -> THE
    CB -> TB -> likely TO meaning B -> O
    '''
    ciphertext = ciphertext.replace('D', ' ')

    # Our substitutions dictionary to keep track of what becomes what when decrypting
    substitutions = dict()

    # The character substitutions, for tracking and use in the automated switching
    substitutions['A'] = 'V'
    substitutions['B'] = 'O'
    substitutions['C'] = 'T'


    substitutions['F'] = 'F'
    substitutions['G'] = 'M'
    substitutions['H'] = 'H'
    substitutions['I'] = 'N'
    substitutions['J'] = 'W'
    substitutions['K'] = 'S'
    substitutions['L'] = 'K'
    substitutions['M'] = 'Y'
    substitutions['N'] = 'I'
    substitutions['O'] = 'L'
    substitutions['P'] = 'R'
    substitutions['Q'] = 'B'
    substitutions['R'] = 'G'
    substitutions['S'] = 'E'
    substitutions['T'] = 'C'

    substitutions['V'] = 'A'
    substitutions['W'] = 'X'

    substitutions['Y'] = 'D'
    substitutions['Z'] = 'P'
    substitutions['|'] = 'U'

    plaintext = replace(ciphertext, substitutions)
    words = plaintext.split(' ')
    print(collections.Counter(words).most_common())
    print(plaintext)

    # For the sake of the output and check lets add back the | character
    plaintext = plaintext.replace(' ', '|')
    return plaintext


if __name__ == '__main__':
    # Test cases
    ciphertext = 'SVCDCHNILSPKDVIYDSVPISKCOMDVZZSVODCBDCHSGDVKDFSOOBJDGVIDCBDFSOOBJDGSIDVIYDVKLDCHSGDCBDCSOODHNGDCHSNPDGSCHBYDHNKDGBBYDCPVIKG|CSYDNCKSOFDNICBDVDYBRRSYDNIYNFFSPSITSDCNOODVCDOSIRCHDHSDFVITNSYDHSDJVKDOBBLNIRDBIDHNKDBJIDSWNKCSITSDJNCHDCHSDZVKKNASDNICSPSKCDBFDVIDB|CKNYSPDHSDJVKDSGQNCCSPSYDQMDCHSDTBIANTCNBIDCHVCDVOODCHNKDYSKBOVCNBIDHVYDQSSIDQPB|RHCDVQB|CDQMDCHSDVTTNYSICDBFDHSPDQSNIRDVDY|PQSPANOOSDJHSIDHSDFB|IYDCHVCDCSKKDTVGSDBFDCHVCDSWHV|KCSYDVITNSICDONISDVIYDJVKDIBCDBFDCHSDISJDCPNQSKDFPBGDQSOBJDVKDHSDHVYDFBIYOMDYPSVGSYDJHMDHVYDHSDIBCDKCBNTVOOMDVQVIYBISYDHSPDNIDFNYSONCMDCBDHNKDZPNITNZOSKDCHNKDJVKDJHVCDHSDHVYDRBCDQMDVZBKCVKMDVIYDHNKDZ|INKHGSICDJVKDYSKSPASYDCHSIDHSDQSTVGSDJSVPMDVIYDVIWNB|KDVIYDHNKDVIWNSCMDNITPSVKSYDHSDJBIYSPSYDNFDHSDHVYDCPSVCSYDHSPD|IFVNPOMDHSDVCSDJNCHB|CDLIBJNIRDCHVCDHSDVCSDVIYDYPVILDJNCHB|CDCVKCNIRDVKDCHSDHB|PKDYPBZZSYD'

    pt = decrypt(ciphertext)

    print(pt[0:30])
    print(pt)

    # Essentially a lazy alternative to manually checking for English text from the results
    with open('/Users/saptarshinath/Desktop/tess27.txt') as file:
        contents = file.read()
        if pt in contents:
            print('Match Found')

        print()
