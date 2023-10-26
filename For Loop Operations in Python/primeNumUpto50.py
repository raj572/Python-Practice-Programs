#Find Prime Numbers: Write a program that finds and prints all prime numbers between 1 and 50 using a for loop.

lower=int(input('Enter starting number : '))
upper=int(input('Enter last number : '))
print(f"These are the all prime numbers between {lower} and {upper}")
for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)
