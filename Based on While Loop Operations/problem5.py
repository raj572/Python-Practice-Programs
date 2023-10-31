#5. Table of a Number: Print the multiplication table of a number (e.g., 9) from 1 to 10 using a while loop.
start=1
end=10
while start<=end:
    i=1
    print()
    print(f'Table of {start}')
    print()
    while i<=10:
        print(f'{start} X {i} = {start*i}')
        i+=1
    start+=1
    
