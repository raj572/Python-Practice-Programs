'''
ABCDE
1234
ABC
12
A

ascii value of a is 65
we will use chr() to convert ascii value to character value
'''
n=int(input('Enter number of rows : ')) #input 5 for required result
for row in range(n,0,-1):
    for col in range(row):
        if row%2==0:
            print(col+1,end='')
        else:
            print(chr(65+col),end='')
    print()
    