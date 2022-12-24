
def file_exists():

    file_exists = True

    try:
        f = open('content/prime_numbers.txt', 'r')
    except:
        file_exists = False

    return file_exists

def generate_prime_numbers():

    counter = 0

    prime_numbers = []

    for i in range(100, 200):
        for j in range(1, 200):
            if (i/j).is_integer() == True:
                counter += 1
        if counter == 2:
            prime_numbers.append(i)
        counter = 0

    return prime_numbers

def write_file(regen):

    print('\n[*] Searching prime numbers file in directory content.')
    
    exists = file_exists()

    if exists == False or regen == True:

        try:
            f = open('content/prime_numbers.txt', 'x')
            print('[*] Creating file.')
        except:
            pass

        try: 
            print('[*] Calculating prime numbers. This could take a while...')
            prime_numbers = generate_prime_numbers()
            f = open('content/prime_numbers.txt', 'w')
            print('[*] Writing prime numbers to file.\n')
            for x in prime_numbers:
                f.write('%d\n' % x)
            f.close()
        except Exception as e:
            raise e
