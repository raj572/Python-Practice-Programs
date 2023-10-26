'''
   *
  * *
 * * *
* * * *
 * * *
  * *
   *
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
