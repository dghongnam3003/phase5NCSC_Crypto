from itertools import cycle
from binascii import hexlify, unhexlify

hex1 = "1a3d4f"
hex2 = "e7"

print(hexlify(bytes(x ^ y for x, y in zip(unhexlify(hex1), cycle(unhexlify(hex2))))))