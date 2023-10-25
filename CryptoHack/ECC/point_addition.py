from Crypto.Util.number import *

a = 497
b = 1768
d = 9739

# (a) If P = O, then P + Q = Q.
# (b) Otherwise, if Q = O, then P + Q = P.
# (c) Otherwise, write P = (x1, y1) and Q = (x2, y2).
# (d) If x1 = x2 and y1 = −y2, then P + Q = O.
# (e) Otherwise:
#   (e1) if P ≠ Q: λ = (y2 - y1) / (x2 - x1)
#   (e2) if P = Q: λ = (3x12 + a) / 2y1
# (f) x3 = λ2 − x1 − x2,     y3 = λ(x1 −x3) − y1
# (g) P + Q = (x3, y3)

def point_addition(p, q):
    if p == (0, 0):
        return q
    if q == (0, 0):
        return p
    
    x1, y1 = p
    x2, y2 = q
    if x1 == x2 and y1 == -y2:
        return (0, 0)
    
    lamba = 0
    if p == q:
        lamda = ((3*pow(x1, 2, d))+a)*inverse(2*y1, d)
    else:
        lamda = ((y2-y1)*pow(x2-x1, -1, d))
    
    x3 = (lamda**2 - x1 - x2)%d
    y3 = (lamda*(x1 - x3) - y1)%d
    
    return (x3, y3)

P = (493, 5564)
Q = (1539, 4742)
R = (4403,5202)

S = point_addition(P, (point_addition(P, point_addition(Q, R))))

print(S)