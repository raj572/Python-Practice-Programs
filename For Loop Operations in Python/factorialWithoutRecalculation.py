# Factorial without Recalculation: Calculate the factorial of a number using a for loop, but optimize it by not re-calculating factorials you've already computed.
n = int(input("Enter a number: "))
if n < 0:
    print("Factorial is not defined for negative numbers")
else:
    factorials = [1]  # Initialize a list to store computed factorials, starting with 0!

    for i in range(1, n + 1):
        next_factorial = factorials[-1] * i
        factorials.append(next_factorial)

    result = factorials[-1]
    print(f"The factorial of {n} is {result}")
