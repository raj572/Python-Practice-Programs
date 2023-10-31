# Write a program to count the number of even and odd numbers from a series of numbers.
start=int(input('Enter first number of series : '))
end=int(input('Enter last number of series : '))
odd=0
even=0
for i in range(start,end+1):
    print(i,end=' ')
    if i%2==0:
        even+=1
    else:
        odd+=1
print()
print(f'There are {odd} odd numbers and {even} even numbers in this series')