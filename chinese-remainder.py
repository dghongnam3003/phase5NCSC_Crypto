base = [2, 3, 5]
modulos = [3, 5, 7]

def chinese_remainder(base_lst, mod_lst):
    M = 1
    M_lst = []
    for x in base_lst:
        M *= x
    
    for i in range (len(mod_lst)):
        M_lst.append(1)
        tmp = [x for x in mod_lst]
        mod_lst.remove(mod_lst[i])
        print(mod_lst)
        for j in mod_lst:
            M_lst[i] *= j
        mod_lst = tmp
    for i in M_lst:
        print(i)
chinese_remainder(base, modulos)