#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 19:04:04 2021

@author: sultan
"""

total_cost = float(input('Enter the total cost of your house: '))
annual_salary = float(input('Your annual income: '))/12
portion_saved = float(input('What portion of your annual income are you willing to save?: '))
portion_down_payment = 0.25*total_cost
current_savings = 0
r = 0.04

months = 0
while current_savings <= portion_down_payment:
    months += 1
    current_savings += annual_salary*portion_saved + (current_savings*0.04)/12 


print(f'It will take you around {months/12:.1f} years for your first down payment')