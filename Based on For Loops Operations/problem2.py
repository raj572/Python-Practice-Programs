text = input('Enter text : ')

uppercase_letters = ""

for char in text:
    if char.isupper():
        uppercase_letters += char

print("Uppercase letters in the string:", uppercase_letters)
