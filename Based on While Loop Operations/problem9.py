'''
 Palindrome Checker: Create a program that checks if a given word 
 or phrase is a palindrome (reads the same forwards and backward) using a while loop.
'''
word=input('Enter word or phrase : ')
i=0
temp=''
while i<len(word):
    temp=word[i]+temp
    i+=1
print(f'''
Given word is {word}
Reverse word of given word is {temp}''')

if temp==word:
    print('Given word is palindrome.It means we are getting same word from forword or backword')
else:
    print('Given word is not palindrome.It means we will not get same word from forword or backword')