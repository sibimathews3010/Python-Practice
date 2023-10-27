def check_vowel_or_consonant(char):
    vowels = "AEIOUaeiou"

    if char.isalpha() and len(char) == 1:
        if char in vowels:
            return "Vowel"
        else:
            return "Consonant"
    else:
        return "Invalid input. Please enter a single alphabet."

# Get input from the user
char = input("Enter a single alphabet: ")

# Check if the character is a vowel or consonant
result = check_vowel_or_consonant(char)

# Print the result
print("The character is:", result)
