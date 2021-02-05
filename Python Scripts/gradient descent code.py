# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oFt6De37JR2UFlma0f5vcJclKbgC1G20
"""

import math
import numpy as np
def vecLength(v): 
  tempSum = 0.0 
  for x in v: 
    tempSum += x[0]**2 
  return math.sqrt(tempSum)

def f(A,b,x,y): 
  temp = np.matrix([[x],[y]]) 
  return np.matrix(np.dot(A,temp)-b)

def grad(A,b,x,y): 
  vec = np.matrix([[x],[y]]) 
  return np.matrix(2*np.dot(np.transpose(A),np.dot(A,vec)-b))

def main(): 
  gamma = .01
  A = np.matrix([[3,1],[2,-1]]) 
  b = np.matrix([[-1],[1]])
  x = .5 
  y = -.5 
  step = 0 
  while vecLength(f(A,b,x,y)) > .05: 
    step += 1 
    x = (np.matrix([[x],[y]]) - gamma*grad(A,b,x,y)).item(0) 
    y = (np.matrix([[x],[y]]) - gamma*grad(A,b,x,y)).item(1) 
    print("(x,y) = (",x,", ",y,")") 
    print("The magnitude of the output of f at step ", step, " is " , vecLength(f(A,b,x,y)), "\n")
main()