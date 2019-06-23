import sys


def encrypt(plaintext, output_file, a, b):
    plaintext_file = open(plaintext, 'r')
    encrypted_file = open(output_file, 'w')
    temp_text = plaintext_file.read()
    for c in temp_text:
        d = ((a * ord(c)) + b) % 127
        encrypted_file.write(chr(d))


def decrypt(ciphertext, output_file, a, b):
    ciphertext_file = open(ciphertext, 'r')
    decrypted_file = open(output_file, 'w')
    temp_text = ciphertext_file.read()
    inverse_a = modinv(a, 127)
    for c in temp_text:
        d = ((ord(c) - b) * inverse_a) % 127
        decrypted_file.write(chr(d))


def decipher(ciphertext, output, dictionary):
    dictionary_string = open(dictionary, 'r').read()
    max_num, a, b = 0, 0, 0
    for test_a in range(1, 126):
        for test_b in range(0, 126):
            decrypt(ciphertext, output, test_a, test_b)
            temp_max = 0
            with open(output, 'r') as f:
                for line in f:
                    for word in line.split():
                        if filter(str.isalnum, word.lower()) in dictionary_string \
                                and filter(str.isalnum, word).__len__() > 3:
                            temp_max += 1
            if temp_max > max_num:
                max_num, a, b = temp_max, test_a, test_b
    decrypt(ciphertext, output, a, b)
    deciphered_text = open(output, 'r').read()
    output_file = open(output, 'w')
    output_file.truncate(0)
    output_file.write("%d %d\nDECIPHERED MESSAGE:\n%s" % (a, b, deciphered_text))

    print "%d %d\n%s\n%d" % (a, b, deciphered_text, max_num)


def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def main():
    mode = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]

    if mode == "encrypt":
        a = int(sys.argv[4])
        b = int(sys.argv[5])
        if a >= 127 or a < 0 or b >= 127 or b < 0:
            print "The key pair (%d, %d) is invalid, please select another key." % (a, b)
            return 1
        encrypt(input_file, output_file, a, b)
    elif mode == "decrypt":
        a = int(sys.argv[4])
        b = int(sys.argv[5])
        if a >= 127 or a < 0 or b >= 127 or b < 0:
            print "The key pair (%d, %d) is invalid, please select another key." % (a, b)
            return 1
        decrypt(input_file, output_file, a, b)
    elif mode == "decipher":
        dictionary_file = sys.argv[4]
        decipher(input_file, output_file, dictionary_file)


if __name__ == '__main__':
    main()
