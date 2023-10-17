'''
Write a program in python to calculate and print the electricity bill of a given customer. The customer ID, name, and unit consumed by the user should be captured from the keyboard to display the total amount to be paid to the customer.
The charge are as follow :

Unit Charge/unit
upto 199 @1.20
200 and above but less than 400	@1.50
400 and above but less than 600	@1.80
600 and above @2.00
If bill exceeds Rs. 400 then a surcharge of 15% will be charged and the minimum bill should be of Rs. 100/-
'''
customerID=input('Enter Customer ID : ')
customerName=input('Enter Customer Name : ')
consumedUnit=int(input('Enter Consumed Unit by Customer : '))
chargePerUnit=0 #Default value
# Determine the charge per unit based on units consumed
if consumedUnit<=199:
    chargePerUnit=1.20
elif consumedUnit>=200 or consumedUnit<400:
    chargePerUnit=1.50
elif consumedUnit>=400 or consumedUnit<600:
    chargePerUnit=1.80
else:
    chargePerUnit=2

#calculate the total bill
totalBill=consumedUnit*chargePerUnit

#Apply surcharge 15% if total bill exceeds Rs 400
if totalBill>400:
    surcharge=totalBill*0.15
    totalBill+=surcharge
#Ensuring total bill to be Rs 100
if totalBill==100:
    totalBill=100
print(f"""
      ----Electricity Bill-----
      Customer Name : {customerName}
        Customer ID : {customerID}
        Unit consumed by customer : {consumedUnit}
        Charge Per Unit : {chargePerUnit}
    Total Payble Amount : {totalBill}""")

