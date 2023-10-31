#7. Find Prime Numbers with While Loop: Write a program to find and print all prime numbers between 1 and 100 using a while loop.
lower = 1
upper = 100
print(f"Prime numbers between {lower} and {upper} are:")

num = lower
while num <= upper:
    if num > 1:
        i = 2
        while i < num:
            if num % i == 0:
                break
            i += 1
        else:
            print(num, end=' ')
    num += 1



