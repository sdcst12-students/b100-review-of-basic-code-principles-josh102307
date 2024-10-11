"""
### Assignment 1
#### Calculation of Simple Interest
The simple interest formula is I = P*r*t where I = the amount of interest, P is the principal or the amount invested, r is the interest rate per year (converted to a decimal) and t is the length of time in years.
Write a program that calculates the amount of simple interest for an investment.

Criteria:
Your program should ask the user for 
* an initial investment
* the annual interest rate as a percentage
* the length of time.
  * the user should have the option of entering in the length of time in years, months or days
* The program will calculate the amount of interest earned and display it.
* Appropriate formatting of the output is a requirement for this assignment
"""

import math

principal = float(input("enter initial investment: "))
rate = float(input("enter annual interest rate as a percentage: "))
rate2 = rate/100
time = float(input("enter length of investment in years: "))
interest = principal*rate2*time
futurevalue = principal + interest
print(f"your interest after {time} years at {rate}% is {interest}")
print(f"your future value after {time} years at {rate}% is {futurevalue}")
