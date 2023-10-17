'''
Input any character from the keyboard, WAP to find that whether its a vowel or consonant.
'''
# Input a character from the keyboard
char = input("Enter a character: ")

# Check if the input is a single character and a letter
if len(char) == 1 and char.isalpha():
    if char in ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']:
        print(f"{char} is a vowel.")
    else:
        print(f"{char} is a consonant.")
else:
    print("Invalid input. Please enter a single alphabetic character.")
