#Reverse a String: Write a program to reverse a given string using a for loop.
string=input('Enter string : ')
reversed_string=''
for char in string:
    reversed_string=char+reversed_string
print(f'Reverse string of {string} is {reversed_string}')

'''
Example Output
Enter string : sunny
Reverse string of sunny is ynnus
'''