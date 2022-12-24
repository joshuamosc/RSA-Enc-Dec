
from . import parse_msg_num
from colorama import Fore, init

init()

def encrypt(message, public_key):

    if len(public_key) != 2:
        #print(Fore.RED + '\n[x] Public key must have 2 numbers. Got %d\n' % len(public_key)) // Ya está controlado en rsa.py
        quit() 

    nummessage = parse_msg_num.parse_message(message)

    encrypted_message = [(pow(x, public_key[0])%public_key[1]) for x in nummessage]
        
    return "+".join(map(str, encrypted_message))

def decrypt(encmessage, private_key):

    if len(private_key) != 2:
        #print(Fore.RED + '\n[x] Private key must have 2 numbers. Got %d\n' % len(private_key)) // Ya está controlado en rsa.py
        quit() 

    nummessage = encmessage.split('+')

    decrypted_nummessage = [(pow(int(x), private_key[0])%private_key[1]) for x in nummessage]

    try:
        decrypted_message = parse_msg_num.parse_numbers(decrypted_nummessage)
    except:
        print(Fore.RED + "\n[x] Couldn't decrypt...\n")
        quit()

    return decrypted_message
