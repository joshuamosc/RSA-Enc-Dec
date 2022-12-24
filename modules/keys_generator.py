from . import random_numbers, coprime_calculator
from colorama import Fore, init

init()

def generate_keys():

    prime_numbers = random_numbers.pick_two_random_numbers()

    print(Fore.LIGHTCYAN_EX +"\n[*]" + Fore.RESET + " Generating keys, please wait...\n")

    p = int(prime_numbers[0])
    q = int(prime_numbers[1])

    n = p*q
    f = (p-1)*(q-1)
    e = coprime_calculator.get_coprime(f)[0]
    d = pow(e, -1, f)
    
    print(Fore.LIGHTGREEN_EX + "[*] Public Key:" + Fore.RESET + " %d,%d" % (e, n))
    print(Fore.LIGHTRED_EX + "[*] Private Key:" + Fore.RESET + " %d,%d\n" % (d, n))
