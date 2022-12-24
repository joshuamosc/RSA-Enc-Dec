
import signal
from modules import keys_generator, prime_numbers_generator, enc_dec_message, args_controller

# Ctrl + C

def def_handler(sig, frame):
    print('\n\n[x] Exiting... \n')
    quit()

signal.signal(signal.SIGINT, def_handler)

if __name__ == '__main__':

    # Args

    args = args_controller.args()

    # Generations

    if args.generate_keys:
        prime_numbers_exist = prime_numbers_generator.file_exists()
        if prime_numbers_exist == False:
            prime_numbers_generator.write_file(False)
        keys_generator.generate_keys()
    if args.generate_prime:
        prime_numbers_generator.write_file(True)

    # Encryption and decryption

    if args.encrypt != None:
        if args.e != None and args.n != None:
            encrypted_message = enc_dec_message.encrypt(args.encrypt, [args.e, args.n])
            print('\n[*] Message encrypted successfully!\n')
            print('%s\n\n' % encrypted_message)
        else:
            print('\n[!] You need to provide the public key correctly. Use the parameter -h to get more help\n')
    
    
    if args.decrypt != None:
        if args.d != None and args.n != None:
            decrypted_message = enc_dec_message.decrypt(args.decrypt, [args.d, args.n])
            print('\n[*] Message decrypted successfully!\n')
            print('%s\n\n' % decrypted_message)
        else:
            print('\n[!] You need to provide the private key correctly. Use the parameter -h to get more help\n')