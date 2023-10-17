#Create a Python program that asks the user to input their age Based on their age,provide the following output:
#if the age is less than 18, print 'you are a minor'. if the age is between 18 and 65 (inclusive), print 'YOu are an adult.
#if the age is 66 or older,print "You are a senior citizen."

age=int(input('Enter age : '))
if age>=0 and age<18:
    print('You are Minor.')
elif age>=18 and age<=65:
    print("You are an adult.")
elif age>66:
    print('You are a senior citizen.')
else:
    print('Invalid age number!')