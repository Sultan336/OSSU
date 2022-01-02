#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 15:24:31 2021

@author: sultan
"""

x = 25
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low)/2.0
while abs(ans**3 - x) >= epsilon:
    print(f'low =  {low:.3f}, high =  {high:.3f} ans =  {ans:.3f}')
    #print(f'ans**2= {ans**2:.3f} ans**2-x= {ans**2 - x:.3f}, epsilon= {epsilon:.3f}')
    numGuesses +=1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('numGuesses =', numGuesses)
print(ans, 'is close to square root of', x)
