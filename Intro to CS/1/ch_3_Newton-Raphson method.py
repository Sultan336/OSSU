#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 19:42:03 2021

@author: sultan
"""

#Newton-Raphson for square root
#Find x such that x**2 - 24 is within epsilon of 0
epsilon = 1
k = 27.0 
guess = k/2.0
while abs(guess**2 - k) >= epsilon:
    guess = guess - (((guess**2) - k)/(2*guess))
    print('Square root of', k, 'is about', guess,)
