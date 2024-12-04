'''Exercise 1: Vowel or Consonant'''
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

def check_letter():
    letter = input('Please, type a letter:')
    vowels = ['a', 'e', 'i', 'o', 'u']
    if letter.isalpha():
        if letter in vowels:
            print(f'The letter {letter} is a vowel')
        else :
            print(f'The letter {letter} is a consonant')
    else:
        print('This is not a alphameric character')

# Call the function
# check_letter()

'''Exercise 2: Old enough to vote?'''
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

def check_voting_eligibility():
    try:
        user_input = int(input('Please enter your age:'))
        if user_input > 18:
            print('You are eligible to vote')
        elif user_input < 0:
            print('Negative numbers are invalid')
        else:
            print('You cannot vote yet')
    except ValueError:
        print('Invalid input, please enter a valid integer')
        

# Call the function
# check_voting_eligibility()

'''Exercise 3: Calculate Dog Years'''
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
    try:
        age = int(input("Input a dog's age:"))
        num = 1
        dog_age = 0
        while num <= age:
          print(num)
          if num == 1 or num == 2:
              dog_age += 10
          else:
              dog_age += 7
          num +=1
        print(f"The dog's age in dog years is {dog_age}")
    except:
        print('Invalid input, please enter a valid integer')
    

# Call the function
# calculate_dog_years()

'''Exercise 4: Weather Advice'''
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():
    temp = input('Is it cold outside (yes/no):').lower()
    rain = input('Is it raining (yes/no):').lower()
    if temp == 'yes' and rain == 'yes':
        print("Wear a waterproof coat.")
    elif temp == 'yes' and rain == 'no':
        print("Wear a warm coat.")
    elif temp == 'no' and rain == 'yes':
        print("Carry an umbrella.")
    elif temp == 'no' and rain == 'no':
        print("Wear light clothing.")

# Call the function
# weather_advice()

'''Exercise 5: What’s the Season?'''
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season():
    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    winter = ['dec','jan', 'feb', 'mar']
    spring = ['mar', 'apr', 'may', 'jun']
    summer = ['jun', 'jul', 'aug', 'sep']
    fall = ['sep', 'oct', 'nov', 'dec']
    season = ''
    
    user_month = input('Enter the month of the year as 3 characters:')
    if len(user_month) != 3:
        return print('For month, your input needs to be 3 characters long')
    elif user_month.lower() not in months:
        return print('The month you enter does not exist')

    user_day = input('Enter the day of the month:')
    try:
        day = int(user_day)
    except ValueError:
        return print(f'"{user_day}" is not a valid number')
    if day > 31:
        return print('The number for day is too high')

    if user_month in winter:
        if user_month == 'dec' and day < 21:
            season = 'fall'
        elif user_month == 'mar' and day > 19:
            season = 'spring'
        else:
            season = 'winter'
    elif user_month in spring:
        if user_month == 'mar' and day < 20:
            season = 'winter'
        elif user_month == 'jun' and day > 20:
            season = 'summer'
        else:
            season = 'spring'
    elif user_month in summer:
        if user_month == 'jun' and day < 21:
            season = 'spring'
        elif user_month == 'sep' and day > 21:
            season = 'fall'
        else:
            season = 'summer'
    elif user_month in fall:
        if user_month == 'sep' and day < 22:
            season = 'summer'
        elif user_month == 'dec' and day > 20:
            season = 'winter'
        else:
            season = 'fall'

    print(f'{user_month.lower().capitalize()} {user_day} is in {season.capitalize()}')

# Call the function
determine_season()