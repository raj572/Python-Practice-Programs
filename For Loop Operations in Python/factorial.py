#Factorial: Write a program to calculate the factorial of a number using a for loop.
n=int(input('Enter number to get factorial of it : '))
factorial=1
for i in range(1,n+1):
    factorial=factorial*i
print(f'Factorial of {n} is {factorial}')
