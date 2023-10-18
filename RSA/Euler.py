def gcd(a, b):
    if (a == 0):
        return b
    return gcd(b%a, a)

def phi(n):
    result = 1
    for i in range(2, n):
        if (gcd(i, n) == 1):
            result += 1
            
    return result

print(phi(882564595536224140639625987659416029426239230804614613279163))