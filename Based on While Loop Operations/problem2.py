# 2. Sum of Even Numbers: Calculate the sum of even numbers from 1 to 50 using a while loop.

i=1
sum=0
while i<=50:
    if i%2==0:
        sum+=i
    i+=1
print('Sum of Even numbers from 1 to 50 is ',sum)