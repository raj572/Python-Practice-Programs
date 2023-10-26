'''
program to print this pattern in python

ABCDE
EDCB
ABC
ED
A
'''

for i in range(5, 0, -1):
    if i % 2 == 0:
        start = 69
        end = start - i
        for j in range(start, end, -1):
            print(chr(j), end='')

    else:
        start = 65
        end = 65 + i
        for j in range(start, end):
            print(chr(j), end='')
    print()
