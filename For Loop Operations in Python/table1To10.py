#Print the Multiplication Table: Write a program to print the multiplication table of a number from 1 to 10 using a for loop.

for i in range(1,11):
    for j in range(1,11):
        print(f'{i} X {j} = {i*j}',end='\t')
    print()