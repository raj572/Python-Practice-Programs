number=int(input('Enter number: '))
i=2
flag=0
while i<=number:
    if number%i==0:
        flag+=1
    i+=1
if flag>2:
    print(number,'is not a prime')
else:
    print(number,' is a Prime number')
        
