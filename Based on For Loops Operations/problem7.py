#Write a Python program to print the alphabet pattern 'L'.

n=int(input('Enter number of rows : '))
for i in range(n+1):
    if i==n:
        print('* '*n)
    else:
        print('*')
print()