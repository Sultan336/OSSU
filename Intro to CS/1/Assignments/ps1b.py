#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 19:04:04 2021

@author: sultan
"""

total_cost = float(input('Enter the total cost of your house: '))
annual_salary = float(input('Your annual income: '))
portion_saved = float(input('What portion of your annual income are you willing to save?: '))
semi_annual_raise = float(input('Your semi-annual raise: '))
portion_down_payment = 0.25 * total_cost
current_savings = 0.0
monthly_rate_of_return = 0.04 / 12
monthly_salary = annual_salary / 12
monthly_deposit = monthly_salary * portion_saved

months = 0
while current_savings <= portion_down_payment:
    months += 1
    current_savings *= 1 +  monthly_rate_of_return
    current_savings += monthly_deposit
    if months % 6 == 0:
        annual_salary *= 1 + semi_annual_raise
        monthly_salary = annual_salary / 12
        monthly_deposit = monthly_salary * portion_saved


print(f'Along with semi-annual raise it take you around {months/12:.1f} years')