import random

def pick_two_random_numbers():

    try:
        f = open('content/prime_numbers.txt', 'r') # No es ../content porque se está llamando a la funcion desde la raiz
        numbers = f.readlines()
        prime_numbers = [x.rstrip('\n') for x in numbers]
        random_numbers = random.choices(prime_numbers, k=2)
    except Exception as e:
        raise e

    return random_numbers
