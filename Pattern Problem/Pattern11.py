'''
    *
   *@*
  *@@@*
   *@*
    *
'''
n = 5  # Adjust this value to control the size of the diamond

for i in range(n):
    for j in range(n):
        if i + j == n // 2 or j - i == n // 2 or i - j == n // 2 or i + j == (n // 2) * 3:
            print("*", end="")
        elif i==1 and j==2:
            print("@", end="")
        elif i==3 and j==2:
            print('@',end='')
        elif i == n // 2 and j == n // 2:
            print('@',end='')
        elif i==2 and j==1 or i==2 and j==3:
            print('@',end='')

        else:
            print(" ", end="")
    print()
