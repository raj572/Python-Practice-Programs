score = int(input('Enter Your score to know your Grade : '))
if score<=100 and score>=90:
    print('Your grade is A')
elif score<=89 and score>=80:
    print('Your grade is B')
elif score<=79 and score>=70:
    print('Your grade is C')
elif score<=69 and score>=60:
    print('Your grade is D')
else:
    print('You are Fail.')