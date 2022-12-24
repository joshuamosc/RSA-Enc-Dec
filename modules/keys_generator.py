from . import random_numbers, coprime_calculator

def generate_keys():

    prime_numbers = random_numbers.pick_two_random_numbers()

    print("\n[*] Generating keys, please wait...\n")

    p = int(prime_numbers[0])
    q = int(prime_numbers[1])

    n = p*q
    f = (p-1)*(q-1)
    e = coprime_calculator.get_coprime(f)[0]
    d = pow(e, -1, f)
    
    print("[*] Public Key: %d,%d" % (e, n))
    print("[*] Private Key: %d,%d\n" % (d, n))
