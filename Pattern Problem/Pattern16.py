'''
*******
 *****
  ***
   *
  ***
 *****
*******
'''
n=int(input())
k=n
d=n//2
for i in range((d)+1):
    print(' '*i+'*'*k)
    k-=2
h=2
for i in range(3):
    print(' '*h+'*'*d)
    d+=2
    h-=1
print()

