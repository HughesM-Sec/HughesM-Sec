import random
import string

def generate_pass(length):
    all_characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
#To ensure you get at least one of each unique character, number, lowercase letter, uppercase letter, special character, I made those the first four it generates.
    password_start = random.choice(string.ascii_lowercase) + random.choice(string.ascii_uppercase) + random.choice(string.digits) + random.choice(string.punctuation)
#Subtract the four characters that we added on at the start so that the character length is correct.
    password_end = ''.join(random.choice(all_characters) for _ in range(length - 4))
    password = password_start + password_end
    password_list = list(password)

# I didn't want the first four characters to always be the same type of unique character, so I added a few shuffles to mix it up.
    for _ in range(3):
        random.shuffle(password_list)
    shuffled_password = ''.join(password_list)
    return shuffled_password

length = int(input("Enter the length of the password: "))
password = generate_pass(length)
print("Generated password:", password)

#So that if it's run directly on Windows you have time to copy down the password before command prompt closes.
str(input("Press any key to close..."))
