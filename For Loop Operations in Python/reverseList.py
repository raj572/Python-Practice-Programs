#Reverse a List: Write a program to reverse a given list using a for loop without using the built-in reverse() function.

lst=[]
n=int(input('Enter number of items to add in list : '))
for i in range(n):
    lst.append(input('Add item : '))
print(f'Create list : {lst}')

reverseList=[]
length=len(lst)
for item in range(length-1,-1,-1):
    reverseList.append(lst[item])
print(f'Reverse List : {reverseList}')
