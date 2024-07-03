# Strings Project: Word Analyzer
# Create a program that takes a word or phrase from the user and provides the following information:

# Number of characters (including spaces)
# Number of characters (excluding spaces)
# The word/phrase in all uppercase
# The word/phrase in all lowercase
# Whether it's a palindrome (reads the same forward and backward, ignoring spaces and punctuation)


phrase = input("Enter your word or phrase: ")
count_with_spaces = len(phrase) # Count the characters including whitespaces
count_without_spaces = len(''.join(filter(str.isalnum, phrase))) # Count without whitespace
def check_palindrome(phrase): # Defining a function to see if the phrase is a palindrome
    phrase = ''.join(filter(str.isalnum, phrase)).lower()
    if phrase:
        return phrase == phrase[::-1] # If the reversed phrase is the same as phrase, True
    else:
        return False
# I wanted each check to start on a new line, I had to do some googling to get this one to work right.
print(f"Lowercase: {phrase.lower()}\nUppercase: {phrase.upper()}\nCount without spaces: {count_without_spaces}\nCount with spaces: {count_with_spaces}")

if check_palindrome(phrase) == True: # I had all this good without reference, except one thing: I had it indented. Tsk.
    print("This is a palindrome.")
else:
    print("This is not a palindrome.")

# This was a confidence builder for my second project. Even on the bits I had to look up for help
# as I saw the solution, I was immediately able to understand why it worked. It didn't look like
# a cat walked over the keyboard to me as usual.