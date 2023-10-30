from itertools import cycle, product
from binascii import unhexlify, hexlify
from math import log
from string import printable
from typing import Iterable

ENGLISH_FREQ = {
    'A' :  8.55,    'K' :  0.81,    'U' :  2.68,
    'B' :  1.60,    'L' :  4.21,    'V' :  1.06,
    'C' :  3.16,    'M' :  2.53,    'W' :  1.83,
    'D' :  3.87,    'N' :  7.17,    'X' :  0.19,
    'E' : 12.10,    'O' :  7.47,    'Y' :  1.72,
    'F' :  2.18,    'P' :  2.07,    'Z' :  0.11,
    'G' :  2.09,    'Q' :  0.10,                 
    'H' :  4.96,    'R' :  6.33,                 
    'I' :  7.33,    'S' :  6.73,                 
    'J' :  0.22,    'T' :  8.94,    
}

def get_score(s: bytes, replace: bool = True, puncts: Iterable[bytes] = b',. \'"\n'):
    # Get the log likelihood of an English string.
    # Parameters:
    # @s          bytestring to be considered
    # @replace    whether to not count valid punctuations in freq analysis
    # @puncts     the punctuations to consider
    #             only required when `replace` is True

    # Effectively, remove punctuations from the strings, so that the normalizing
    # constant is smaller in that case, prioritizing strings with more printables.
    if replace:
        for b in puncts:
            if type(b) is int:
                b = chr(b).encode()
            s = s.replace(b, b'')
    
    return sum(ENGLISH_FREQ[char]*(log(s.count(char.encode()) + s.count(char.lower().encode()) + 1e-12) - log(len(s))) for char in ENGLISH_FREQ)

def stream_xor(b1: bytes, b2: bytes) -> bytes:
    return bytes(x^y for x, y in zip(b1, cycle(b2)))

def brute_xor(cipher: bytes, c_min = 1, c_max = 4, charset: Iterable[bytes] = printable.encode()) -> (bytes, bytes):
    # Parameters:
    #     @cipher     cipher to be decrypted
    #     @c_min      the min length of XOR key
    #     @c_max      the max length of XOR key
    #     @charset    the character set of the key
    # Output:
    #     @max_score  the maximum likelihood
    #     @key        the key used to decrypt
    #     @decrypted  the decrypted text
    
    max_score, max_decrypted, max_key = None, None, None
    for c_len in range(c_min, c_max):
        for key in product(charset, repeat = c_len):
            #broken bytestring
            if type(key[0]) is int:
                key = bytes(key)
            #literal list of bytes
            #helpful when you're trying only a fixed set of possible keys
            else:
                key = b''.join(key)
            decrypted = stream_xor(cipher, key)
            score = get_score(decrypted)
            if max_score is None or score > max_score:
                max_score, max_decrypted, max_key = score, decrypted, key
                
    return max_score, max_decrypted, max_key

hex_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

# Convert the hex string to bytes
cipher_bytes = bytes.fromhex(hex_string)

# Call the brute_xor function to find the decryption
max_score, key, decrypted_text = brute_xor(cipher_bytes)

# Print the results
print("Likelihood score:", max_score)
print("Decryption key:", key.decode())  # Decode the key from bytes to a string
print("Decrypted text:", decrypted_text.decode())