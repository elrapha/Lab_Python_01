"""
Zeller’s algorithm computes the day of the week on which a given date will fall (or fell). In
this exercise, you will write a program to run Zeller’s algorithm on a specific date. You
will need to create a new file for this program, zellers.py. The program should use the
algorithm outlined below to compute the day of the week on which the user’s birthday fell
in the year you were born and print the result to the screen.

Let A, B, C, D denote integer variables that have the following values:
A = the month of the year, with March having the value 1, April the value 2, ... December
the value 10, and January and February being counted as months 11 and 12 of the
preceding year (in which case, subtract 1 from C)
B = the day of the month (1, 2, 3, ... , 30, 31)
C = the year of the century (e.g. C = 89 for the year 1989)
D = the century (e.g. D = 19 for the year 1989)
Note: if the month is January or February, then the preceding year is used for
computation. This is because there was a period in history when March 1st, not January
1st, was the beginning of the year.
"""

A=raw_input('Enter month as a number between 1 and 12 where March is 1 and Feb is 12: ')

B=raw_input('Enter the day of the month as numbers between 1 and 31: ')

year=raw_input('Enter year (eg. 1999): ')

A=int(A)
B=int(B)
C=int(year)%100
D=int(year)/100

if A==11:
    print '11th month'
    C=C-1
if A==12:
    print '12th month'
    C=C-1


# print A,' ',B,' ',C,' ',D

W = (13*A - 1) / 5
X=C/4
Y=D/4
Z = W + X + Y + B + C - 2*D
R=Z % 7

R=R%7

print A+2,'/',B,'/',year,' falls on',R 










