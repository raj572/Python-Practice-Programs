'''
    1
   1 2
  1   3
 1     4
1 2 3 4 5
'''
n=5
k=2
a=1
b=2
c=2
for i in range(1,n+1):
    for j in range(1,n*2):
        if i+j==n+1:
            print(a,end='')
        elif j-i==n-1:
            print(c,end='')
            c+=1
        elif j!=k and i==n:
            print(b,end='')
            b+=1
            k+=2
        else:
            print(end=' ')
    print()