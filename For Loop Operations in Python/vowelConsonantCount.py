#Count Vowels and Consonants: Create a program that counts the number of vowels and consonants in a given string using a for loop.

string = input('Enter words: ')
vowel = 0
consonant = 0
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

for char in string:
    if char.isalpha():  # Check if the character is alphabetic (not a space or other special character)
        if char in vowels:
            vowel += 1
        else:
            consonant += 1

print("Vowels:", vowel)
print("Consonants:", consonant)



