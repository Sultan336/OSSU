#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 23:12:31 2022

@author: sultan
"""

def fib(n):
    """Assumes n int >= 0
    Returns fibonacci of n """
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
def testFib(n):
    for i in range(n+1):
        print('fib of', i, '=', fib(i))
testFib(2)