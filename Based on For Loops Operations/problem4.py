#Write a program to check whether the given number is positive and divisible by 5 or not.
n=int(input('Enter number : '))
if n>0 and n%5==0:
    print(f'{n} is positive and divisible by 5')
elif n>0 and n%5!=0:
    print(f'{n} is postive but not divisible by 5')
elif n<0 and n%5==0:
    print(f'{n} is negative and divisible by 5')

else:
    print(f'{n} is negative and not divisible by 5')