'''
program to print this pattern

ABCDEFEDCBA
ABCDE EDCBA
ABCD   DCBA
ABC     CBA
AB       BA
A         A
'''
li=[]
alpha=65
n=int(input('Enter number of rows : '))
for i in range(n):
    li.append(chr(alpha))
    alpha+=1
alpha-=2
for i in range(n-1):
    li.append(chr(alpha))
    alpha-=1
l=len(li)
fh=(l//2)-1
lh=int((l//2)+1)
for i in range(n):
    print(*li)
    if ' ' not in li:
        li[l//2]=' '
    else:
        li[fh]=' '
        li[lh]=' '
        fh-=1
        lh+=1
    

  