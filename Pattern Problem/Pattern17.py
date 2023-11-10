'''
write  a program to print this pattern 

ABCDEFEDCBA
ABCDE EDCBA
ABCD   DCBA
ABC     CBA
AB       BA
A         A
AB       BA
ABC     CBA
ABCD   DCBA
ABCDE EDCBA
ABCDEFEDCBA
'''
n=int(input('Enter any number : '))
for i in range(n):
    for j in range(n-i):
        print(chr(65+j), end = "")
    print(" "*i, end = "")
    print(" "*(i-1), end = "")
    for k in range(n-i, 0, -1):
        if k ==n:
            continue
        print(chr(65+k-1), end ="")
    print()

for m in range(2,n+1):
    for j in range(m):
        print(chr(65+j),end='')
    print(" "*(n-m), end = "")
    print(" "*((n-1)-m), end = "")
    for d in range(m):
        if d == 0 and m == n:
            continue
        print(chr(65+m -d-1), end = "")
    print()