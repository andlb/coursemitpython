# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 18:58:03 2017

@author: aborges
"""

#object: data abstraction that capture internal representation or an interface for interaction with object
class CoordinateClass(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def distance(self,other):
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq  + y_diff_sq  ) ** 0.5

    def __str__(self):
        return "CoordinateClass..:"+str(self.x) + str(self.y)
   # def __add__(self,other):
   # def __sub__(self,other):
    def __eq__(self,other):
        return other.x == self.x
    def __lt__(self,other):
        return other.x < self.x
    def __len__(self):
        return self.x*self.y
c = CoordinateClass(3,4)
zero = CoordinateClass(0,0)
print(c.distance(zero))
print(c)
#verify if object is an instance of a class
print(isinstance(c,CoordinateClass))