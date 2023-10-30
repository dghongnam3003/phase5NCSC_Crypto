from binascii import unhexlify
import string

def single_byte_xor(input, key):
    if len(chr(key)) != 1:
      raise "KEY LENGTH EXCEPTION: In single_byte_xor key must be 1 byte long!"

    output = b''
    for b in input:
        output += bytes([b ^ key])

    try:
        return output.decode("utf-8")
    except:
        return "Cannot Decode some bytes"

data = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
decoded = unhexlify(data)

print("[-] HEX_DECODE: {}\n".format(decoded))

result = {}
for i in range(256):
    result[i] = (single_byte_xor(decoded, i))
    #print("[-] KEY: {}\nSTRING: {}".format(i,single_byte_xor(decoded, i)))


print("[*] FLAG: {}".format([s for s in result.values() if "crypto" in s]))