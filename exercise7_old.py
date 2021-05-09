from collections import Counter

import re

ALPHABET = [chr(i) for i in range(65, 91)]  # A-Z capitals inclusive


def incrementer(string, steps):
    return ''.join(ALPHABET[(ALPHABET.index(i) + steps) % len(ALPHABET)] for i in string)


#  https://gist.github.com/carlsmith/b2e6ba538ca6f58689b4c18f46fef11c
def replace(string, substitutions):
    substrings = sorted(substitutions, key=len, reverse=True)
    regex = re.compile('|'.join(map(re.escape, substrings)))
    return regex.sub(lambda match: substitutions[match.group(0)], string)


ALPHABET.append("|")  # Add the vertical bar to the alphabet for this exercise as we are using tess27
ENCRYPTED = 'SVCDCHNILSPKDVIYDSVPISKCOMDVZZSVODCBDCHSGDVKDFSOOBJDGVIDCBDFSOOBJDGSIDVIYDVKLDCHSGDCBDCSOODHNGDCHSNPDGSCHBYDHNKDGBBYDCPVIKG|CSYDNCKSOFDNICBDVDYBRRSYDNIYNFFSPSITSDCNOODVCDOSIRCHDHSDFVITNSYDHSDJVKDOBBLNIRDBIDHNKDBJIDSWNKCSITSDJNCHDCHSDZVKKNASDNICSPSKCDBFDVIDB|CKNYSPDHSDJVKDSGQNCCSPSYDQMDCHSDTBIANTCNBIDCHVCDVOODCHNKDYSKBOVCNBIDHVYDQSSIDQPB|RHCDVQB|CDQMDCHSDVTTNYSICDBFDHSPDQSNIRDVDY|PQSPANOOSDJHSIDHSDFB|IYDCHVCDCSKKDTVGSDBFDCHVCDSWHV|KCSYDVITNSICDONISDVIYDJVKDIBCDBFDCHSDISJDCPNQSKDFPBGDQSOBJDVKDHSDHVYDFBIYOMDYPSVGSYDJHMDHVYDHSDIBCDKCBNTVOOMDVQVIYBISYDHSPDNIDFNYSONCMDCBDHNKDZPNITNZOSKDCHNKDJVKDJHVCDHSDHVYDRBCDQMDVZBKCVKMDVIYDHNKDZ|INKHGSICDJVKDYSKSPASYDCHSIDHSDQSTVGSDJSVPMDVIYDVIWNB|KDVIYDHNKDVIWNSCMDNITPSVKSYDHSDJBIYSPSYDNFDHSDHVYDCPSVCSYDHSPD|IFVNPOMDHSDVCSDJNCHB|CDLIBJNIRDCHVCDHSDVCSDVIYDYPVILDJNCHB|CDCVKCNIRDVKDCHSDHB|PKDYPBZZSYD'
TESS27 = open("/Users/saptarshinath/Desktop/tess27.txt").readline()

tessMostCommon = Counter(TESS27).most_common()
tessMostCommonWords = Counter(TESS27.split('|')).most_common()
encryptedMostCommon = Counter(ENCRYPTED).most_common()
print(tessMostCommonWords)
print(encryptedMostCommon)

replacements = {}
for index in range(len(ALPHABET)):
    replacements[encryptedMostCommon[index][0]] = tessMostCommon[index][0]

print(replacements)

replacements["B"] = "A"
replacements["Y"] = "T"

replacements["D"] = "T"
replacements["Y"] = "O"

replacements["Y"] = "H"
replacements["K"] = "O"

replacements["K"] = "N"
replacements["Z"] = "O"

replacements["J"] = "O"
replacements["Z"] = "S"

replacements["G"] = "F"
replacements["V"] = "P"

replacements["O"] = "R"
replacements["Q"] = "I"

replacements["X"] = "G"
replacements["H"] = "W"

replacements["T"] = "W"
replacements["H"] = "M"

replacements["S"] = "B"
replacements["F"] = "Y"

replacements["V"] = "U"
replacements["M"] = "P"

replacements["H"] = "K"
replacements["A"] = "M"

replacements["F"] = "P"
replacements["M"] = "Y"

replacements["A"] = "V"
replacements["C"] = "M"

replacements["M"] = "M"
replacements["C"] = "Y"

replacements["I"] = "Z"
replacements["U"] = "X"

#print(replacements)

decrypted = CipherUtils.replace(ENCRYPTED, replacements)
words = decrypted.split("|")

#print(tessMostCommonWords)
#print(Counter(words).most_common())