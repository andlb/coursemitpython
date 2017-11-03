# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 18:34:18 2017

@author: aborges
"""

try:
    a = int(input("type a number"))
    b = int(input("type a number"))
    c = a/b
except:
    print("You have to type a number")
    #when you want to recieve the error in the other method.
    raise ValueError("there was an error when the user type the input")