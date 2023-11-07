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
n=11
k=n//2
for i in range(n):
    for j in range(k):
        print(chr(65+j),end='')
    for j in range(k,-1,-1):
        print(chr(65+j),end='')

    print()
  










