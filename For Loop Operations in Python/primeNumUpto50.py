#Find Prime Numbers: Write a program that finds and prints all prime numbers between 1 and 50 using a for loop.
'''
print("Prime numbers between 1 and 50:")
start=1
end=50
for number in range(start+1,end):
    for i in range(2,number+1):
        if number%i==0:
            break
    if i==number:
        print(number)
'''
#second method
print("Prime numbers between 1 and 50:")

for number in range(2, 51):
    is_prime = True
    sqrt_num = int(number ** 0.5) #or you can write int(number ** 1/2)

    for i in range(2, sqrt_num + 1):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(number)
