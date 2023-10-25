hex1 = '1c0111001f010100061a024b53535009181c'
hex2 = '686974207468652062756c6c277320657965'

bytes1 = bytes.fromhex(hex1)
bytes2 = bytes.fromhex(hex2)

print(hex(int(hex1, 16)^int(hex2, 16)))