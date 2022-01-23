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

def isPalindrome(s):
    """ Assumes s is str
        Returns True if letters in s form a palindrome;
        False otherwise. 
        Non-letters and capitalization are ignored"""
    def toChars(s):
        s = s.lower()
        letters = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                letters += c
        return letters
    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            answer = s[0] == s[-1] and isPal(s[1:-1])
            print(f'About to return {answer} for {s} ')
            return answer
    return isPal(toChars(s))
    
def testIsPalindrome():
    print('Try dogGod')
    print(isPalindrome('dogGod'))
    print('Try doGood')
    print(isPalindrome('doGood'))
testIsPalindrome()

    
            