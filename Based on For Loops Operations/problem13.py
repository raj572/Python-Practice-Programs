#Write a program to find Cumulative sum of a list

li=[]
n=int(input('Enter number of elements : '))
for i in range(n):
    li.append(int(input('Enter element to add : ')))
sum=0
cumulativeSumList=[]
for i in li:
    sum+=i
    cumulativeSumList.append(sum)
print('Original List : ',li)
print('Cumulative Sum of List : ',cumulativeSumList)
    