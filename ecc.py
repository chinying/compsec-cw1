from copy import deepcopy

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return str(self.x) + ", " + str(self.y)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

class EllipticCurve:
    def __init__(self, a, b, k, points=None):
        self.a = a
        self.b = b
        self.k = k
        self.points = points if points is not None else {}

    def __str__(self):
        return "y^2 = x^3 + " + str(self.a) + "x + " + str(self.b)

    def _y(self, x):
        return (x**3 + self.a * x + self.b)

    def onCurve(self, x, y):
        return (self._y(x)) % self.k == (y ** 2) % self.k

    def add(self, p, q):
        if p == q:
            m = ((3 * (p.x ** 2) + self.a) % self.k) * (self.modinv(2 * p.y, self.k)) % self.k
        else:
            m = (((p.y - q.y) % self.k) * self.modinv(p.x - q.x, self.k)) % self.k
        xr = (m**2 - p.x - q.x) % self.k
        yr = -(q.y + m * (xr - q.x)) % self.k
        return Point(xr, yr)

    def mult(self, p, n): # nice TODO use the doubling thing like fast exp, speeds up from linear to log
        tmp = deepcopy(p) # idk enough about this but deep copy just in case
        for i in range(n-1): # needs to -1, just think about it
            # print(i, p, tmp)
            p = self.add(p, tmp)
        return p

    def modinv(self, a, m):
        r, s, t = 1, 0, a
        u, v, w = 0, 1, m
        while w != 0:
            q = t // w
            u, v, w, r, s, t = (r - q * u), (s - q * v), (t - q * w), u, v, w
        return r % m

    def order(self, p): # brute force, prime is so small anyway
        i = 0
        tmp = deepcopy(p)
        while True:
            if self.onCurve(p.x, p.y) is False:
                break
            p = self.add(p, tmp)
            i += 1
        return i + 1 # include point at infinity

    def insertPoint(self, point):
        self.points.add(point)

# k = 103

# """example"""

# p = Point(19 ,97)
# q = Point(27, 81)
# E = EllipticCurve(a = -2, b = 13, k = 103)
# print(E)
# print("R : (%s) " % E.add(p, q))
# print(E.mult(p, 3))
# print(E.order(p))
# """end example"""
