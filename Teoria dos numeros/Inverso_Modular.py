def extEuclid(a, b):
    xx, y = 0, 0
    yy, x = 1, 1
    while b != 0:
        q = a // b
        a, b = b, a % b
        xx, x = x - q * xx, xx
        yy, y = y - q * yy, yy
    return a, x, y

def mod(a, m):
    return ((a % m) + m) % m

def modInverse(b, m):
    d, x, y = extEuclid(b, m)
    if d != 1:
        return -1  
    return mod(x, m) 
