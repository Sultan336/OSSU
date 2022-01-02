#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 15:01:28 2021

@author: sultan
"""

x = 123456
epsilon = 0.01
step = epsilon**3
numGuesses = 0
ans = 0.0
while abs(ans**2 -x) >= epsilon and ans**2 <=x:
    ans += step
    numGuesses += 1
print('numGuesses = ',numGuesses)
if abs(ans**2 - x) >= epsilon:
    print('Failed on the square root of', x)
else:
    print(ans, 'is close to square root of', x)