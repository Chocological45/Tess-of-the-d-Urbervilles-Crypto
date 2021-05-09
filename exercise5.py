def decrypt(ciphertext):
    plaintext_list = dict()

    # Loop for all possible number of columns (4 to 6)
    for col in range(4, 6):

        # Get the maximum length of the columns for the 'table'
        col_len = int(len(ciphertext) / col)

        # Format the ciphertext for use in transposition decryption
        # Essentially using column number and column length with start : stop syntax in list comprehension
        columns = [ciphertext[i*col_len : i*col_len+col_len] for i in range(col)]

        # Formatting to find the decrypted plaintext
        plaintext = ''
        for letter in range(len(columns[0])):
            for row in range(len(columns)):
                plaintext += columns[row][letter]


        # Add the decrypted plaintext to the list of possible decryptions
        plaintext_list[col] = plaintext

    return plaintext_list


if __name__ == '__main__':
    # Test cases
    ciphertext = 'RIRGFRCHWTKYNPGLNREEOEASLOETICYSAIRBSEHESIENALORDEAMITNEBUWOETWOTEEAYFSAVWEATORNNAETUHROENHOEEASHBSLTHPIAENOEHDERHOTLEWNFNENEANICWAFWSTTEWBGOTLTNTATEOENPUWIELYHCEOEDORNNLCINEMTHTETREETNTTWAONDUNTESHGIEELOSGTLYAENMMYDEEAHIOERCDAERRUBTEIFFESRLOMEEAMIATFLRCRAWSSRIALTDDYSHWCEENHBUMYIUSEHTFUFCTDNLSCESRCTEKSPCIEUIYIEACRDOVRELDHEAOESADETYDDGILEAITATATREREWOAHIFDOTLRTARANROWOORNHTTAAEPEODGPHEADHFSMOOHHENUDRRGEPEEANSFDGSJAOASBFIEOENRSINUWUHOTTEETEEENAFATAOFISADINTTAYEEGNNAOERNLSTEHEOAARRCEAXIONCIREIEROOYITPOHWETOYTTERHNILMNNIRUSITEAHOHIRNALHSIRTWEOANEISDERHCAOLIWEUTAGOORTOSHSELGYWIUNSEIHHSFRRSNTLSAOIOEASEDTAERXSSENLRADMITAIPRIUSWNRYONOUSTEINGASNIFUHWYHLDDGNEROCTFLASANTRYMWOLEDENWDYBEAHBOSNRRSEEDYFLUDHEYRSAEUUACHIMTOFHUSOHROETRKPOTRTLHDLHSAVETTDLSEIFEHARNISNTSARDAOGFLDHNTETHRCMWVIETSKVSLTTVEBNEEIUAOSAHIETBNFICEDEETYEIAATIAHSTANHMERENSSLDE'

    pt_list = decrypt(ciphertext)

    # Essentially a lazy alternative to manually checking for English text from the results
    for col, pt in pt_list.items():
        print(pt[0:30])
        print(str(col) + ": " + pt)

        with open('/Users/saptarshinath/Desktop/tess26.txt') as file:
            contents = file.read()
            if pt in contents:
                print('Match Found')

            print()
