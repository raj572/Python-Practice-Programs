'''lst=[]
n=int(input('Enter number of items '))
for i in range(n):
    lst.append(int(input('Enter number : ')))
def find_maximum(lst):
    if len(lst) == 0:
        return None  # Return None for an empty list
    
    maximum = lst[0]  # Initialize the maximum with the first element of the list
    
    for num in lst:
        if num > maximum:
            maximum = num  # Update the maximum if a larger number is found
    
    return maximum

def find_minimum(lst):
    if len(lst) == 0:
        return None  # Return None for an empty list
    
    minimum = lst[0]  # Initialize the minimum with the first element of the list
    
    for num in lst:
        if num < minimum:
            minimum = num  # Update the minimum if a smaller number is found
    
    return minimum
print("List item : ",lst)
print('Maximum value = ',find_maximum(lst))
print('Minimum value = ',find_minimum(lst))'''


lst = []
n = int(input('Enter number of items you want to add in list '))

for item in range(n):
    lst.append(int(input(f'Enter {item + 1}th item ')))

lst.sort()  # Sort the list in ascending order
print('Your created list : ', lst)

target = int(input('Enter the number you want to find '))


def binary_search(lst, target):
    right = n - 1  # Adjust the right pointer
    left = 0

    while left <= right:
        mid = (left + right) // 2

        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return f'{target} is not in {lst}'


index = binary_search(lst, target)
print(f'Target {target} is at index {index}')
print('Minimum value in the list is ',lst[0])
print('Maximum value in the list is ',lst[-1])