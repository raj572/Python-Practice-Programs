#Write a program to enter any week day number and print day.
weekDayDict={
    1:'Sunday',
    2:'Monday',
    3:'Tuesday',
    4:'Wednesday',
    5:'Thursday',
    6:'Friday',
    7:'Saturday'
}

dayNumber=int(input('Enter any week day number to print equiavalent day : '))
if dayNumber in weekDayDict:
    print(f'{weekDayDict[dayNumber]}')
else:
    print('Your entered week day number is out of range')