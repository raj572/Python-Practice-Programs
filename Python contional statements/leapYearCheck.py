'''
A year is a leap year if the following conditions are satisfied: 

The year is multiple of 400.
The year is a multiple of 4 and not a multiple of 100.
'''

year = int(input('Enter year in number : '))
if year%400==0 or (year%4==0 and year%100!=0):
    print(year,' is a leap year.')
else:
    print(year,' is not a leap year.')
