from math import sqrt
# note that bits are in reverse order
def bits(x):
    b = []
    while x:
        b.append(x & 1)
        x = x >> 1
    return b

def multinv(a, m):
    r, s, t = 1, 0, a
    u, v, w = 0, 1, m
    while w != 0:
        q = t // w
        u, v, w, r, s, t = (r - q * u), (s - q * v), (t - q * w), u, v, w
    return r % m

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def lcm(a, b):
    return (a * b) / gcd(a, b)

def isPrime(x):
    if x <= 1:
        return False
    if x <= 3:
        return True
    if (x % 2 == 0) or (x % 3) == 0:
        return False
    for i in range(5, int(sqrt(x) + 1), 6):
        if (x % i == 0) or (x % (i + 2) == 0):
            return False
    return True
