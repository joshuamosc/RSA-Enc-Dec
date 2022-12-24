import argparse

def args(): 

    # Args 

    parser = argparse.ArgumentParser(
        prog='RSA Enc-Dec',
        description='This is a RSA encryptor, where you need a public key to encrypt a message, and a private key to decrypt it. The public and private key consists of 2 numbers. You will need to pass the values of the variables e and n to encrypt a message or d and n to decrypt it',
        epilog='© 2023 Negtune'
    )

    parser.add_argument('-gk', '--generate-keys', action='store_true', help='Generates private and public keys for later use', required=False)
    parser.add_argument('-gp', '--generate-prime', action='store_true', help='Generates prime numbers in a file in ./content', required=False)
    parser.add_argument('-enc', '--encrypt', action='store', type=str, help='Encrypts a message using e and n', metavar='MESSAGE', required=False)
    parser.add_argument('-dec', '--decrypt', action='store', type=str, help='Decrypts a message using d and n', metavar='MESSAGE ENCRYPTED', required=False)
    parser.add_argument('-e', action='store', type=int, help='e is the first number of your public key, e < n, required to encrypt', required=False)
    parser.add_argument('-n', action='store', type=int, help='n is the second number of your key, d < n > e, required to enc and dec', required=False)
    parser.add_argument('-d', action='store', type=int, help='d is the first number of your private key, d < n, required to decrypt', required=False)

    args = parser.parse_args()

    return args
