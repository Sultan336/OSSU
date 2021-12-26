#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 14:57:34 2021

@author: sultan
"""

mysum = 0
for i in range(5,11,2):
    mysum += i
    if mysum ==5:
        break
        mysum += 1
print(mysum)

