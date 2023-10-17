# Find the Largest Number: Write a program that takes a list of numbers and finds the largest number in the list using a for loop.

numList = []
n = int(input('How many numbers do you want to add to the list? Please enter: '))
for number in range(n):
    numList.append(int(input('Enter item: ')))

print(numList)

largest = numList[0]  # Initialize the largest number to the first element in the list

for i in numList:
    if i > largest:
        largest = i

print("The largest number in the list is:", largest)
