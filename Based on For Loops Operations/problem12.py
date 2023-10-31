#Python program to print odd numbers in a List.

li=[]
n=int(input('Enter number of elements : '))
for i in range(n):
    li.append(int(input('Enter element to add : ')))
print(f'List : {li}')
odd_numbers=[]
for i in li:
    if i%2!=0:
        odd_numbers.append(i)
print(f'The List of Odd numbers from given list is {list(set(odd_numbers))}')
