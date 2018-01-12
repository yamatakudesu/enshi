# -*- coding: utf-8 -*-
import math

def sign(x):
    if (x > 0):
        return 1.0
    elif (x < 0):
        return -1.0
    else:
        return 0


a = 1.0
b = -100000.0
c = 1.0

x1 = (- b - math.sqrt(b*b - 4*a*c))/2*a
x2 = (- b + math.sqrt(b*b - 4*a*c))/2*a

print("a = %27.20e" % a)
print("b = %27.20e" % b)
print("c = %27.20e" % c)
print("x1 = %27.20e" % x1)
print("x2 = %27.20e" % x2)
print("e1 = %27.20e" % (a*x1*x1+b*x1+c))
print("e2 = %27.20e" % (a*x2*x2+b*x2+c))

x1_ = (- b + sign(b)*math.sqrt(b*b - 4*a*c))/2*a
x2_ = c / (a * x1_)
print("x1'= %27.20e" % x1_)
print("x2'= %27.20e" % x2_)
print("e1'= %27.20e" % (a*x1*x1+b*x1+c))
print("e2'= %27.20e" % (a*x2*x2+b*x2+c))
