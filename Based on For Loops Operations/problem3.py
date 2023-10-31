#Write a program to find the common elements in two lists using a for loop.

list1=input('Enter elements seperated by space to add in first list : ').split()
list2=input('Enter elements seperated by space to add in second list : ').split()

common_elements=[]

for item1 in list1:
    for item2 in list2:
        if item1 == item2:
            common_elements.append(item1)

if common_elements:
    print(f'These is the list of common elements of both lists  {list(set(common_elements))}')
else:
    print('There is not any common elements in these two lists.')
