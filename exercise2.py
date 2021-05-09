def decrypt(ciphertext):
    # Key: TESSOFTHEDURBERVILLES

    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key = 'TESSOFTHEDURBERVILLES'
    plaintext = ''

    # Find the shift between ciphertext character, and the character from the key, then find the new
    # character for the plaintext result
    for i in range(len(ciphertext)):
        new_pointer = (alphabet.find(ciphertext[i]) - alphabet.find(key[i % len(key)])) % 26
        plaintext += alphabet[new_pointer]

    return (plaintext)


if __name__ == '__main__':
    # Test cases
    pt = decrypt('RWSQAWLKYUVVSZZGTPDEQLXZSHXALA')

    print(pt[0:30])
    print(pt)

    # Essentially a lazy alternative to manually checking for English text from the results
    with open('/Users/saptarshinath/Desktop/tess26.txt') as file:
        contents = file.read()
        if pt in contents:
            print('Match Found')

        print()
