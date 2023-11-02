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
k=4
for i in range(11):
    for j in range(6):
        print(chr(65+j),end=' ')
    for j in range(10,5,-1):
        print(chr(65+k),end=' ') 
        k-=1     
    print()











