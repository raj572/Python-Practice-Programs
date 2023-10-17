#Multiplication Table: Create a program that takes an integer input from the user and prints its multiplication table from 1 to 10 using a for loop.

number=int(input('Enter number to print table of it ----> '))
for i in range(1,11):
    print(f'{number} X {i} = {number*i}')
    