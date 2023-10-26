'''
program to print this pattern

ABCDEFEDCBA
ABCDE EDCBA
ABCD   DCBA
ABC     CBA
AB       BA
A         A
'''
a1=[]
c=65
n=int(input('Enter number of rows : '))
for i in range(n):
    a1.append(chr(c))
    c+=1
c-=2
for i in range(n-1):
    a1.append(chr(c))
    c-=1
l=len(a1)
fh=int((l/2)-1)
lh=int((l/2)+1)
for i in range(n):
    print(*a1)
    if ' ' not in a1:
        a1[int(l/2)]=' '
    else:
        a1[fh]=' '
        a1[lh]=' '
        fh-=1
        lh+=1
    

  