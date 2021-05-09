import itertools


def decrypt(ciphertext):
    plaintext_list = dict()

    # Given a column length of 6
    key_length = 6
    # Get all the possible permutations of the key for key length 6
    keys = list(itertools.permutations([0, 1, 2, 3, 4, 5]))

    # Get the maximum length of the columns for the 'table'
    col_len = int(len(ciphertext) / key_length)

    # Format the ciphertext for use in transposition decryption
    # Essentially using column number and column length with start : stop syntax in list comprehension
    columns = [ciphertext[i*col_len : i*col_len+col_len] for i in range(key_length)]

    # For all the key combinations possible
    for combo in keys:
        # Define an empty plaintext
        # This is important as for each combination we will need a clean plaintext variable
        plaintext = ''

        # Start creating our decrypted strings for each key combination
        for row in range(col_len):
            for col in combo:
                plaintext += columns[col][row]

        # Append our decrypted string to the list of possible decryptions
        plaintext_list[combo] = plaintext

    return plaintext_list


def permutations(list_of_values):
    # Return all the possible permutations of a given list of values
    return list(itertools.permutations(list_of_values))


if __name__ == '__main__':
    # Test cases
    ciphertext = 'ADNIENRAEONTEARNTDIYHRHLHSHEMDTPKNERWSDNAMERNIOESRLRESEIGRMTHNTSTHIANEAOTTHAEWAAMECSNHWTDRISIETRLELLHFTSEIEEEGNDSHEAAVCLPSHANTELTOHEHSGGAYCRIMLFCSIRNDEMTIUIEIREUBLEDHAIGTAIADAVSSOMCAAMINDNDTAHOINFEWNBIOAOLAONTENDNWSINOHRHFFLNRNSAPLEYTEEOCAAOAEIRCTRNTIAIANANNHTESTDDICFLTTYNHIMEGBHNAEOARHOOEKOESSTWTETORLDETEHATWSBIFESDHOLHEISONIOFHTMNEINSEDHTEPIHPONLOAIOISOICETEOEAAANNMIRBODHSIHFTESSEOIEESTSHFODAITSZAAAEHTRWEHBITHEBNYOTTESVCETEWDORREHOENTDVAAABONEAHLSGLTOEFGRAEEUMNDOHEHDIASIEBHEDOIYITSAADTOHILRHSPEAASSOSITAMESRHOOSEIEHHMDLFSTNHTEERIGERLHTENTHVLTUALEESHVWKXMIIHEISMSTAEHNRONNMLGEECTICSEOSMCIBESAEALDDPOHCUOEDEVNCHREUYTUMSITSWERHNGIWCVNWHERAEICEANOYSHHADFTDLTONAVHSVCAOIMSDGDOEADESHOMLEIHTTGONIPMAEEHSFEEFIMACGAECEUTAHUIDRTRFGNYEELOIERCREEDPSPATTAEFEOLSEEBEERRFBTSIUBSHHDHMCSIPSRKRMEFEOERPDMSTPGSTNSIUSTLFCOAEOLPENARYIRHHDOAEOLGTLRTHTIATL'

    pt_list = decrypt(ciphertext)

    # Essentially a lazy alternative to manually checking for English text from the results
    # Unlike with previous exercises, there are 720 key permutations so we will just output the one
    # combination that produces the correct plaintext.
    for col, pt in pt_list.items():
        with open('/Users/saptarshinath/Desktop/tess26.txt') as file:
            contents = file.read()
            if pt in contents:
                print(pt[0:30])
                print(str(col) + ": " + pt)
                print('Match Found')
