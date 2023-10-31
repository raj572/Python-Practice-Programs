# 6. Collatz Sequence: Write a program that generates the Collatz sequence starting from a given number using a while loop. The sequence should end when it reaches 1.

'''
It concerns sequences of integers in which each term is obtained from the previous term as follows: if the previous term is even, the next term is one half of the previous term. If the previous term is odd, the next term is 3 times the previous term plus 1.
'''

n=int(input('Enter number : '))
while n>1:
    if n%2==0:
        n=n//2
        print(n,end=' , ')
    else:
        n=3*n+1
        print(n,end=' , ')