# Factorial with While Loop: Calculate the factorial of a number using a while loop.

n=int(input('Enter number to find its factorial : '))
fact=1
i=1
while i<=n:
    fact*=i
    i+=1
if n<0:
    print('Invalid number to get factorial!')
elif n==0:
    print(f'Factorial of {n} is 1')
else:
    print(f'Factorial of {n} is {fact}')