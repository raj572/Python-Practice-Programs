'''
1@2@3
@2@3
2@3
@3
3
'''
# First Method

s=''
j=1
n=5
for i in range(1,n+1):
    if i%2!=0:
        s+=str(j)
        j+=1
    else:
        s+='@'
for i in range(1,n+1): 
    print(s[i-1:])
   


'''
Start

Initialize variables:

a (total number of rows) = 5
j (counter for the inner loop) = 1
m (a temporary variable for printing numbers) = 0
k (a variable for adjusting the starting value of m) = 1
Loop for i from 1 to a (inclusive):
a. Check if i is even:

Increment k by 1.
Set m to k.
b. Loop for j from 1 to a - i + 1:
i. Check if i is odd and j is even or if i is even and j is odd:
- Print "@".
ii. Otherwise:
- Print the value of m.
- Increment m by 1.

c. Move to the next line to start a new row.

End
'''
#second method

# a=5
# j=1
# m=0
# k=1
# for i in range(1,a+1):
#     if i%2==0:
#         k+=1
#     m=k
#     for j in range(1,a-i+2):
#         if i%2!=0 and j%2==0 or i%2==0 and j%2!=0:
#             print('@',end='')
#         else:
#             print(m,end='')
#             m+=1
#     print()
