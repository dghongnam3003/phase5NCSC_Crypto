import math

base = [2, 3, 5]
modulos = [5, 11, 17]

def chinese_remainder(base_lst, mod_lst):
    M = 1
    M_lst = []
    y_lst = []
    r = 0
    res = 0
    for x in mod_lst:
        M *= x
    
    for i in range (len(mod_lst)):
        M_lst.append(1)
        tmp = [x for x in mod_lst]
        mod_lst.remove(mod_lst[i])
        print(mod_lst)
        for j in mod_lst:
            M_lst[i] *= j
        mod_lst = tmp
    
    for i in range (len(mod_lst)):
        y_lst.append(1)
        y_lst[i] = pow(M_lst[i], -1, mod_lst[i])
        
    for i in range (len(base_lst)):
        r += base_lst[i]*M_lst[i]*y_lst[i]
    res = pow(r, 1, M)
    
    return res

print(chinese_remainder(base, modulos))