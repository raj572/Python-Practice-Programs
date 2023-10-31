'''
Print a Triangle with While Loop: Write a program to print
a right-angled triangle of asterisks (*) where the user inputs
the height of the triangle using a while loop.

*
**
* *
*  *
*****
'''
n = int(input("Enter the height of the triangle: "))

# Initialize a counter for the rows
row = 1

while row <= n:
    col = 1  # Initialize a counter for the columns
    
    while col <= row:
        if col == 1 or col == row or row == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
        col += 1
    
    print()  # Move to the next line for the next row
    row += 1
