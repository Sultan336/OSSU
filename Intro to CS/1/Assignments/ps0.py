#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 16:53:05 2021

@author: sultan
"""
from numpy import log2

x= input('Enter a number X:')
y= input('Enter a another number Y: ')
x,y=int(x), int(y)
print(f'{x} raised to the power {y} is {x*y}')
print(f'The log (base 2) of {x} is {log2(x)} ')