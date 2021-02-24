import math
a, b, h, m = map(int, input().split(" "))
h_ = h*360/12 + m*360/12/60
m_ = m*360/60
# print(h_, m_)
sub = abs(h_ - m_)
c_2 = a**2 + b**2 - 2*a*b*math.cos(math.radians(sub))
print(math.sqrt(c_2))
