'''
ABCDE
FGHI
JKL
MN
O
'''
n=5
k=1
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(chr(64+k),end='')
        k+=1
    print()
