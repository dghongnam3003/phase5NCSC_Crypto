import hashlib
import random
from Crypto.Cipher import AES

# /usr/share/dict/words from
# https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words
with open("C:\\Users\\nampr\\OneDrive\\Documents\\phase5\\AES\\words.txt") as f:
    words = [w.strip() for w in f.readlines()]
keyword = random.choice(words)

KEY = hashlib.md5(keyword.encode()).digest()

def decrypt(ciphertext, password_hash):
    ciphertext = bytes.fromhex(ciphertext)
    key = password_hash

    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return decrypted

l = len(words)

for i in range(l):
    KEY = hashlib.md5(words[i].encode()).digest()
    decrypted = decrypt("c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66", KEY)
    if b'crypto' in decrypted:
        print(decrypted)