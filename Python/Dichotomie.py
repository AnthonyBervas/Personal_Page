#-*- coding: utf-8 -*-
import numpy as np

def dichotomie(xp, xn, f, epsilon=1e-4):
    if np.abs(f(xp) - f(xn)) <= epsilon:
        return ((xp + xn)/2)
    else:
        xm = (xp + xn)/2
        if f(xm)*f(xn) <= 0:
            return dichotomie(xm, xn, f, epsilon)
        elif f(xp)*f(xn) <= 0:
            return dichotomie(xp, xm, f, epsilon)

def f(x):
    return -5*x + 10

a = dichotomie(0, 10, f)

print("xm = ", a)
