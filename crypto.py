from pwn import *
from Crypto.Util.number import *

hex_data = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'

bytes_data = bytes.fromhex(hex_data)

print(bytes_data)

def bytes_xor(input, key):
    if len(chr(key)) != 1:
        raise "KEY LENGTH EXCEPTION: In single_byte_xor key must be 1 byte long!"
    output = b''
    for i in input:
        output += bytes([i^key])

    try:
        return output.decode("utf-8")
    except:
        return "Error"

res = {}
for i in range(256):  #because we xor with single bytes (8 bits), it in range 0 to 256
    res[i] = bytes_xor(bytes_data, i)

print(s for s in res.values() if "crypto" in s)