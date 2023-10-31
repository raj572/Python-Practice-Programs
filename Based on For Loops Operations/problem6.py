# Write a Python program to convert a month name to a number of days.

# Create a dictionary mapping month names to the number of days
monthDaysDict = {
    "January": 31,
    "February": "28 or 29", 
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31,
}

# Input the month name from the user
month = input("Enter the month name: ")

# Convert the input to title case to handle variations in capitalization
month = month.title()

# Check if the month name is in the dictionary
if month in monthDaysDict:
    days = monthDaysDict[month]
    print(f"The number of days in {month} is {days}.")
else:
    print("Invalid month name. Please enter a valid month.")

