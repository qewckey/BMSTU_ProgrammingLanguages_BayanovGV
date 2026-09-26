from math import *

a = float(input('Введите параметр а: '))

y = cos(a) + cos(2*a) + cos (6*a) + cos(7*a)
print("{0:.2f} {1:.2f}".format(a, y))

y = 4*cos(a/2) * cos((5/2)*a) * cos(4*a)
print("{0:.2f} {1:.4f}".format(a, y))
