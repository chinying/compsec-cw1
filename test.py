from copy import deepcopy
from ecc import Point, EllipticCurve
# p = Point(5,1)
# k = 17
# E = EllipticCurve(a = 2, b = 2, k = k)
# t_inf = (E.mult(p, 19))
# # print(E.onCurve(t_inf.x, t_inf.y))
# # print(E.onCurve(p.x, p.y))

# q = Point(6, 3)
# q_inf = (E.mult(q, 19))
# print(E.onCurve(q_inf.x, q_inf.y))

k = 149
E = EllipticCurve(a = -4, b = 10, k = k)
p = Point(29, 61)
# print(E.onCurve(p.x, p.y))
print(E.order(p))
