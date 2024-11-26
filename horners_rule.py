# -*- coding: utf-8 -*-
"""Horners Rule.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14gO3qpoBNZ7w7HhYphoVD_i93NfROpfZ
"""

def horners(poly, x, n):
    result = poly[0]
    for i in range(1, n):
        result = result * x + poly[i]
    return result

poly = [5,4,3,2,-1,-7] # f(x) = x**3-4*x**2+x+6
x = 3
n = len(poly)

print(f"Value of ploynomial is {horners(poly,x,n)}")
