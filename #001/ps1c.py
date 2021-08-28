# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 15:44:09 2021

@author: AbdElRahman ElGharib
"""


def check_portion_saved(annual_salary: float,portion_saved: float) ->tuple:

    semi_annual_raise = 0.07
    current_savings = 0.0
    monthly_salary = annual_salary / 12
    months = 0
    r = 0.04


    while current_savings < portion_down_payment * total_cost:
        
        if months != 0 and months % 6 == 0:
            annual_salary += semi_annual_raise * annual_salary
            monthly_salary = annual_salary / 12
        
        months += 1
        current_savings += r * current_savings / 12 + portion_saved * monthly_salary
        
    return (months, current_savings)

annual_salary = float(input('Enter Starting Annual Salary:\n'))

total_cost = 1E6
portion_down_payment = 0.25
goal_months = 36
min_value = 0.0
max_value = 1.0
portion_saved = (min_value + max_value) / 2

months = check_portion_saved(annual_salary, max_value)[0]

if months > goal_months:
    print('Impossible Mission!')
else:
    
    months, current_savings = check_portion_saved(annual_salary, portion_saved)
    steps = 1
    
    while months != goal_months or abs(current_savings - portion_down_payment * total_cost) >= 100:
        
        if months > goal_months:
            min_value = portion_saved
            portion_saved = (min_value + max_value) / 2
        else:
            max_value = portion_saved
            portion_saved = (min_value + max_value) / 2
        
        months, current_savings = check_portion_saved(annual_salary, portion_saved)
        steps += 1

    print('Recommended portion to save is:',str(round(portion_saved * 100, 2)) + '%')
    print('\n Number of Bisectin Steps is:',steps)