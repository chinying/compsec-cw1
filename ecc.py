from copy import deepcopy
import miscmath

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return str(self.x) + ", " + str(self.y)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __hash__(self):
        return hash((self.x, self.y)) 

class EllipticCurve:
    def __init__(self, a, b, k, points=None):
        self.a = a
        self.b = b
        self.k = k
        self.points = points if points is not None else set() 

    def __str__(self):
        return "y^2 = x^3 + " + str(self.a) + "x + " + str(self.b)

    def _y(self, x):
        return (x**3 + self.a * x + self.b)

    """checks if on the curve"""
    def onCurve(self, x, y):
        return (self._y(x)) % self.k == (y ** 2) % self.k

    def add(self, p, q):
        if p.x == 0 and p.y == 0:
            return q
        if q.x == 0 and q.y == 0:
            return p

        # technically there should be another case where p and q are 0

        if p == q:
            m = ((3 * (p.x ** 2) + self.a) % self.k) * (miscmath.multinv(
                2 * p.y, self.k)) % self.k
        else:
            m = (((p.y - q.y) % self.k) * miscmath.multinv(p.x - q.x, 
                self.k)) % self.k
        xr = (m**2 - p.x - q.x) % self.k
        yr = -(q.y + m * (xr - q.x)) % self.k
        return Point(xr, yr)

    def mult(self, p, n):
        tmp = deepcopy(p)
        q = Point(0, 0)
        bits = miscmath.bits(n)
        for bit in bits:
            if bit == 1:
                q = self.add(q, tmp)
            tmp = self.add(tmp, tmp)
        return q

    def modinv(self, a, m):
        r, s, t = 1, 0, a
        u, v, w = 0, 1, m
        while w != 0:
            q = t // w
            u, v, w, r, s, t = (r - q * u), (s - q * v), (t - q * w), u, v, w
        return r % m

    def order(self): # order
        cnt = 0
        for x in range(self.k):
            for y in range(self.k):
                if self.onCurve(x, y):
                    self.insertPoint(Point(x, y))
                    cnt += 1
        return cnt + 1

    # precondition: you need to provide a point p, and this generates the 
    # subgroup. returns subgroup of points + size
    def sub_order(self, p): 
        i = 1
        tmp = deepcopy(p)
        cycle = set()
        cycle.add(p)
        while True:
            if self.onCurve(p.x, p.y) is False:
                break
            else:
                cycle.add(p)
            p = self.add(p, tmp)
            i += 1
        return (cycle, i)

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
# print(E.order())
# """end example"""
