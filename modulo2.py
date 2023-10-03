import math

def DectoBin(num):
    return bin(num).replace("0b","")

base = 273246787654
res = 1
bin_num = DectoBin(65536)
dividor = 65537

for i in bin_num[::-1]:
    if int(i) == 0:
        base = (base*base) % dividor
    if int(i) == 1:
        res = (res*base) % dividor
        base = (base*base) % dividor

print(res)