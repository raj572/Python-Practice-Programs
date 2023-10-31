# 3. Password Checker: Create a program that asks the user to enter a password and keeps asking until the correct password is entered using a while loop.

entered_password=input('Enter password : ')
correctPassword='1234'
while entered_password!=correctPassword:
    print('Wrong password!')
    entered_password=input('Please enter correct password : ')
else:
    print('Correct Password!')

  