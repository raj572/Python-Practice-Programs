'''
*******
 *****
  ***
   *
  ***
 *****
*******
'''
n=int(input('Enter number of rows : '))
d=n//2
for i in range(d):
    print(' ' * i , '*' * (n-2*i))
m=d+1
k=1
s=1
for i in range(m,0,-1):
    print(' ' * (m-s) ,'*' * k )
    k+=2
    s+=1
print()
