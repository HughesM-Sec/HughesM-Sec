# import datetime
# current_year = datetime.datetime.now().year
# birth_year = current_year - int(age)
# print(f"You were born in approximately {birth_year}.")
name = input("What is your name? ")
try:
    age = float(input("How old are you? "))
except ValueError as e:
    exit("Please enter a valid integer: ")
try:
    height = float(input("How tall are you in meters? "))
except ValueError as e:
    exit("Please enter a valid integer: ")
    # def get_float_input(prompt):
    #     while True:
    #         try:
    #             return float(input(prompt))
    #         except ValueError:
    #             print("Please enter a valid number.")
student = "y" if input("Are you a student? (y/n): ") == "y" else "n"  # Setting the student variable based on user input
if student == "y":
# if student == "y":
#     graduation_year = current_year + (4 - time_elapsed)
#     print(f"You might graduate in {graduation_year}.")
    try: # Used try to handle the error if they put a string in instead of an integer.
        time_elapsed = int(input("What year are you in? 1, 2, 3, 4? "))
        if time_elapsed > 4:
            print("You've already graduated.")
        if time_elapsed == 1:
            print(f"Hello, {name}! You are a {age} year old student, standing {height} meters tall. I hope you enjoy your last 3 years of school!")
        elif time_elapsed == 2:
            print(f"Hello, {name}! You are a {age} year old student, standing {height} meters tall. I hope you enjoy your last 2 years of school!")
        elif time_elapsed == 3:
            print(f"Hello, {name}! You are a {age} year old student, standing {height} meters tall. I hope you enjoy your last year of school!")
        elif time_elapsed == 4:
            print(f"Hello, {name}! You are a {str(age)} year old student, standing {str(height)} meters tall. You're at the finish line, now! Congrats!")
    except ValueError as e:
        print("Invalid input. Please enter an integer between 1 and 4.")
else:
    print(f"Hello, {name}! You are {age} years old and {height} meters tall. You are a not a student at this time.")


    # Improved Version:
    # # Get name (no need for error checking on strings)
    # name = input("What is your name? ")
    #
    # # Get age with error handling
    # while True:
    #     try:
    #         age = float(input("How old are you? "))
    #         break  # Exit the loop if input is valid
    #     except ValueError:
    #         print("Please enter a valid number for age.")
    #
    # # Get height with error handling
    # while True:
    #     try:
    #         height = float(input("How tall are you in meters? "))
    #         break  # Exit the loop if input is valid
    #     except ValueError:
    #         print("Please enter a valid number for height.")
    #
    # # Rest of your code remains the same
    # student = "y" if input("Are you a student? (y/n): ") == "y" else "n"
    #
    # if student == "y":
    #     while True:
    #         try:
    #             time_elapsed = int(input("What year are you in? 1, 2, 3, 4? "))
    #             if 1 <= time_elapsed <= 4:
    #                 break  # Exit the loop if input is valid
    #             else:
    #                 print("Please enter a number between 1 and 4.")
    #         except ValueError:
    #             print("Please enter a valid number between 1 and 4.")
    #
    #     # Your existing code for different years goes here
    #     if time_elapsed == 1:
    #         print(f"Hello, {name}! You are a {age} year old student, standing {height} meters tall. I hope you enjoy your last 3 years of school!")
    #     elif time_elapsed == 2:
    #         print(f"Hello, {name}! You are a {age} year old student, standing {height} meters tall. I hope you enjoy your last 2 years of school!")
    #     elif time_elapsed == 3:
    #         print(f"Hello, {name}! You are a {age} year old student, standing {height} meters tall. I hope you enjoy your last year of school!")
    #     elif time_elapsed == 4:
    #         print(f"Hello, {name}! You are a {age} year old student, standing {height} meters tall. You're at the finish line, now! Congrats!")
    # else:
    #     print(f"Hello, {name}! You are {age} years old and {height} meters tall. You are not a student at this time.")
