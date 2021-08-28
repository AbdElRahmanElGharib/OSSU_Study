# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 17:13:27 2021

@author: AbdElRahman ElGharib
"""

annual_salary = float(input('Enter annual salary:\n'))
portion_saved = float(input('Enter the percentage saved of salary monthly in decimal:\n'))
total_cost = float(input('Enter total cost of the house:\n'))
semi_annual_raise = float(input('Enter Semi-Annual raise in salary:\n'))


current_savings = 0.0
monthly_salary = annual_salary / 12
months = 0
r = 0.04
portion_down_payment = 0.25


while current_savings < portion_down_payment * total_cost:
    if months != 0 and months % 6 == 0:
        annual_salary += semi_annual_raise * annual_salary
        monthly_salary = annual_salary / 12
    months += 1
    current_savings += r * current_savings / 12 + portion_saved * monthly_salary


print('Number of months:' , months)