# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 21:29:12 2021

@author: dkjua
"""
def func1(a):
    i=1
    s=1
    while i<a+1:
        s=i*s
        i=i+1
    return s
x=int(input('數字?'))
print (func1(x))

