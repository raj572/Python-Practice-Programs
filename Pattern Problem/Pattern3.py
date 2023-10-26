'''
    *
   **
  ***
 ****
*****

total rows=5
total space in first row=4
total space in second  row=3
so for space printing we will use ..

space=total rows - i where i=1
star=i
'''
n=int(input('Enter number : '))
for i in range(1,n+1):
    print(' '*(n-i),'*'*i)
