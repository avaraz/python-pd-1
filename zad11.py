from math import sin,cos,tan
a = 0
s = 30
d = 45
f = 90
g = 180

tab1 = [a, s, d, f, g]
tab2 = [sin(a), sin(s), sin(d), sin(f), sin(g)]
tab3 = [cos(a), cos(s), cos(d), cos(f), cos(g)]
tab4 = [tan(a), tan(s), tan(d), tan(f), tan(g)]

print("kąt", tab1)
print("sin", tab2)
print("cos", tab3)
print("tan", tab4)
