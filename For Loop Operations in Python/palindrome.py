#Check for Palindrome: Create a program to check if a given word or phrase is a palindrome using a for loop.

'''
A palindromic number (also known as a numeral palindrome or a numeric palindrome) is a number (such as 16461) that remains the same when its digits are reversed. In other words, it has reflectional symmetry across a vertical axis.
'''
string=input('Enter words or Phrases : ')
length=len(string)
reverseString=''
for char in string:
    reverseString=char+reverseString
if string==reverseString:
    print('Entered words or Phrases is Palindrome.')
else:
    print('It\'s not palindrome.')

