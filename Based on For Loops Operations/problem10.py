# Write a program to merge two Dictionaries.

# Initialize empty dictionaries
dict1 = {}
dict2 = {}

# Input key-value pairs for dict1 from the user
n = int(input("Enter the number of key-value pairs for dict1: "))
for i in range(n):
    key = input("Enter a key for dict1: ")
    value = input("Enter a value for dict1: ")
    dict1[key] = value

# Input key-value pairs for dict2 from the user
m = int(input("Enter the number of key-value pairs for dict2: "))
for i in range(m):
    key = input("Enter a key for dict2: ")
    value = input("Enter a value for dict2: ")
    dict2[key] = value


#printing both dictionary
print(f'First Dictionary : ',dict1)
print(f'Second Dictionary : ',dict2)

# Merge the dictionaries
merged_dict = dict1.copy()
merged_dict.update(dict2)

# Print the merged dictionary
print("Merged dictionary:", merged_dict)
