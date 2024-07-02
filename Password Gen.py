import random
import string

def generate_pass(length):
    all_characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    password_start = random.choice(string.ascii_lowercase) + random.choice(string.ascii_uppercase) + random.choice(string.digits) + random.choice(string.punctuation)
    password_end = ''.join(random.choice(all_characters) for _ in range(length - 4))
    password = password_start + password_end
    password_list = list(password)
    for _ in range(3):
        random.shuffle(password_list)
    shuffled_password = ''.join(password_list)
    return shuffled_password

length = int(input("Enter the length of the password: "))
password = generate_pass(length)
print("Generated password:", password)
str(input("Press any key to close..."))