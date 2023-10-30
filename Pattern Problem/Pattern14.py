'''
     *
    * *
   *   *
  *     *
 *       *
* * * * * *
'''
n=6
k=2
for i in range(1,n+1):
    for j in range(1,n*2):
        if i+j==n+1 or j-i==n-1:
            print('*',end='')
        elif j!=k and i==n:
            print('*',end='')
            k+=2
        else:
            print(end=' ')
    print()