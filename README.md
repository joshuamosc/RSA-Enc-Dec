# RSA - Encryptor and Decryptor

This is a python program that encrypts and decrypts data based in the most basic RSA algorithm, where you have a public key and a private key. The public key is used to encrypt the data, this means that this key can be known by everyone, so they can send data encrypted using your public key. The private key is the key to decrypt the data that has been sent to you.

## Example of keys 
***

```
Public Key -> (e, n) -> (3, 253)
Private Key -> (d, n) -> (147, 253)
```

## How does the RSA algorithm works?
***

The RSA algorithm is based in the factorization of very big prime numbers, and this formula is used.

```
C = Mᵉ mod n
M = Cᵈ mod n

Where:

- C is the ciphered message
- M is the unciphered message
- n is the constant explained in this section
```

First you have to search for 2 prime numbers, it's recommended that these numbers are way too big, in this case: p and q, where p ≠ q

``
p = 11 and q = 23
``

Then we will want the product of these prime numbers and the euler function:

```
n = (p)(q)
f = (p-1)(q-1)

n = (11)(23)
f (11-1)(23-1)

n = 253
f = 220
```

After that, we have to search for an odd number, which is the coprime of ``f``, where 1 < e < ``f``. In this case:

```
e = 3
GCF(3, 220) = 1
```

This means the number 3 and the number 220 don't have common factors, except 1.

Now that we have all these constants, we have to calculate the modular multiplicative inverse of ``e`` and ``f``.

```
d = inv(e, (f))
d * e = 1(f)
```

## Requirements
***

```
Versión mínima Python 3.8
pip3
```

## Installation
***

```sh
git clone https://github.com/joshuamosc/RSA-Enc-Dec.git
cd RSA-Enc-Dec
pip3 install -r requirements.txt
```

## Usage
***

## Generate Private and Public Keys

With this feature you can generate the public and the private keys for later use

```sh
python3 rsa.py --generate-keys
```

or

```sh
python3 rsa.py -gk
```

## Generate prime numbers file

>If the file `prime_numbers.txt` doesn't exist in the directory `./content`, it will be created automatically. Make sure you specify the range of the prime numbers, by default, it's the prime numbers between 100 and 200, but you can change it in `./modules/prime_numbers_generator.py` in the lines 4 and 5.

```python

# Prime numbers range

from_range = 100
to_range = 200

def file_exists():
```

change the variables `from_range` and `to_range`. 

Notes:
 - `to_range` must be bigger than `from_range`
 - The more range there is, the longer the calculation time will be

> If the file already exists, you can regenerate the `prime_numbers.txt` file by using the next command 

```sh
python3 rsa.py --generate-prime
```
or
```sh
python3 rsa.py -gp
```
> If you want to download a file with prime numbers, make sure to follow the next format

```
Filename: prime_numbers.txt
Content format: Line breaks

3
5
7
9
11

```

## Encryptation

To encrypt a message you must use the next command.

> Note: You will need the public key

```sh
python3 rsa.py --encrypt "message super important and confidential" -e xxx -n xxx
```

Where:
- The argument after `-e` is the first number you get in the public key.
- The argument after `-n` is the second number you get in the public key.

> For example
```
Public key: 3, 253
e = 3
n = 253

e < n
```
```sh
python3 rsa.py --encrypt "message super important and confidential" -e 3 -n 253
```

## Decryption

To decrypt a message encrypted you must use the next command.

> Note: You will need the private key

```sh
python3 rsa.py --decrypt "3123+123123+12+33123+123+321+978" -d xxx -n xxx
```

Where:
- The argument after `-d` is the first number you get in the private key.
- The argument after `-n` is the second number you get in the private key.

> For example
```
Private key: 147, 253
d = 147
n = 253

d < n
```
```sh
python3 rsa.py --encrypt "3123+123123+12+33123+123+321+978" -d 147 -n 253
```
