'''
   *
  * *
 * * *
* * * *
 * * *
  * *
   *
'''
n=7
k=n//2
for i in range(k):
    print(' ' * (k-i),'* ' * (i+1))
m=k+1
for j in range(m,0,-1):
    print(' ' * (m-j), '* ' * j)
print()

    


'''
n = 4

# Upper part of the pattern
for i in range(1, n + 1):
    # Print leading spaces
    for j in range(n, i, -1):
        print(" ", end="")
    
    # Print asterisks
    for k in range(1, i + 1):
        print("* ", end="")
    
    print()

# Lower part of the pattern
for i in range(n - 1, 0, -1):
    # Print leading spaces
    for j in range(n, i, -1):
        print(" ", end="")
    
    # Print asterisks
    for k in range(1, i + 1):
        print("* ", end="")
    
    print()
'''