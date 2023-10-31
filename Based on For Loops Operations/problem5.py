#Write a Python program to check if a triangle is equilateral, isosceles or scalene.
first_angle=int(input('Enter first angle value of trangle : '))
second_angle=int(input('Enter second angle value of trangle : '))
third_angle=int(input('Enter third angle value of trangle : '))
if first_angle==second_angle==third_angle:
    print('Equilateral Triangle')
elif first_angle==second_angle or second_angle==third_angle or third_angle==first_angle:
    print('Isosceles Triangle')
else:
    print('Scalene Triangle')