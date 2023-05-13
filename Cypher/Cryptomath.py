def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b

def findModInverse(a, m):
    if gcd(a,m) != 1:
        return None
    u, u1, u2 = 1, 0, a
    v, v1, v2 = 0, 1, m
    while v2 != 0:
         q = u2 // v2
         v, v1, v2, u, u1, u2 = (u - q * v), (u1 - q * v1), (u2 - q * v2), v,v1,v2

    return u % m

