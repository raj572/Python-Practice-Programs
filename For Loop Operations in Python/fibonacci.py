#Fibonacci Sequence: Write a program to generate the first 20 numbers in the Fibonacci sequence using a for loop.


# Number of terms in the Fibonacci series
n = 20

# Initialize the first two Fibonacci numbers
a, b = 0, 1


if n>1:
    print("Fibonacci series up to", n, "terms:")
    count = 0
    for count in range(n):
        print(a, end=" ")
        # Calculate the next term by adding the previous two terms
        nth = a + b
        # Update values for the next iteration
        a = b
        b = nth
        
