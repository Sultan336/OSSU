#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 14:38:05 2022

@author: sultan
"""

print('Figure 4.4 Finding an approximation to a root')
def findRoot(x, power, epsilon):
    """Assume x and epsilon int or float, power an int,
            epsilon > 0 and power >= 1
        Return float y such that y**power is with epsilon of x.
            If such a float does not exists, it returns None"""
    if x < 0 and power%2 == 0:  #Negative number has no even-powered roots.
        return None
    low = min(-1.0, x)
    high = max(1.0, x)
    ans = (high + low)/2
    while abs(ans**power -x) >= epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2.0
    return ans
 
def testFindRoot():
    epsilon = 0.01**2
    for x in [0.25, -0.25, 2, -2, 8, -8]:
        for power in range(1, 4):
            print('Testing x=%s, and power=%s' %(x, power))
            result = findRoot(x, power, epsilon)
            if result == None:
                print(' No root')
            else:
                print(' %s ** %s ~= %s' %(result, power, x))
 
testFindRoot()
# When runs, the code print:
 