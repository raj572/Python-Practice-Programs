number=int(input('Enter number: '))
i=2
check=0
while i<number:
    if number%i==0:
        check+=1
    i+=1
if check==1:
    print(number,'is not a prime')
else:
    print(number,' is a Prime number')
        
