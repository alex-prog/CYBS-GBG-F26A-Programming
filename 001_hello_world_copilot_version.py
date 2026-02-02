"""
001 - Hello World: GitHub Copilot's Version
CYBS-GBG-F26A Programming Course - Spring 2026

This is my enhanced version of the Hello World exercise.
The original instructor file remains unchanged.

Learning Objectives:
- Understand what a Python program is
- Learn how to display output using print()
- Learn how to get input from users using input()
- Understand basic string operations

"""

# ============================================================================
# PART 1: Your First Output
# ============================================================================
# The print() function displays text on the screen
# Whatever you put inside the parentheses will be shown to the user

print('Hello World!')
print("This is GitHub Copilot's version of the first Python program!")
print()  # Empty print() creates a blank line


# ============================================================================
# PART 2: Getting User Input
# ============================================================================
# The input() function asks the user to type something
# The text inside the parentheses is the prompt (question) shown to the user
# The user's answer is stored in a variable (in this case, 'name')

name = input('What is your name? ')
print('Hello', name)
print('Nice to meet you,', name, '!')


# ============================================================================
# PART 3: More Practice with Input and Output
# ============================================================================
# You can ask for different kinds of information

age = input('How old are you? ')
print('Wow,', age, 'years old!')

favorite_color = input('What is your favorite color? ')
print('I like', favorite_color, 'too!')


# ============================================================================
# PART 4: Understanding How It Works
# ============================================================================
"""
Key Concepts:

1. print() - Displays information to the user
   - You can use single quotes: print('text')
   - Or double quotes: print("text")
   - You can print multiple things: print('Hello', name)

2. input() - Gets information from the user
   - Shows a prompt and waits for the user to type
   - Returns the text the user typed (as a string)
   - Store the result in a variable to use it later

3. Variables - Store information for later use
   - Think of them as labeled boxes that hold data
   - Format: variable_name = value
   - Use descriptive names: 'name', 'age', 'favorite_color'

4. Strings - Text data enclosed in quotes
   - Single quotes: 'Hello'
   - Double quotes: "Hello"
   - Both work the same way!
"""


# ============================================================================
# 🎯 EXERCISES
# ============================================================================
"""
Try these exercises to practice what you've learned!
Uncomment the code (remove the # at the start) and complete it.

Exercise 1: Create a program that asks for someone's hometown and prints
a welcoming message.

# hometown = input('Where are you from? ')
# print('Welcome, traveler from', hometown, '!')


Exercise 2: Ask the user for their favorite food and favorite drink,
then print a message combining both.

# food = input('What is your favorite food? ')
# drink = input('What is your favorite drink? ')
# print('Sounds delicious!', food, 'and', drink, 'is a great combination!')


Exercise 3: Create a simple profile program that asks for:
- Name
- Age
- Favorite hobby
Then print all the information together.

# print('=== Create Your Profile ===')
# name = input('Enter your name: ')
# age = input('Enter your age: ')
# hobby = input('Enter your favorite hobby: ')
# print()
# print('=== Your Profile ===')
# print('Name:', name)
# print('Age:', age)
# print('Hobby:', hobby)


Challenge: Make your own creative program using print() and input()!
What questions will you ask? What will you do with the answers?

"""


# ============================================================================
# 💡 TIPS FOR SUCCESS
# ============================================================================
"""
1. Run this program and see what happens!
2. Try changing the text in the print() statements
3. Add your own questions using input()
4. Experiment and have fun!
5. Don't worry about making mistakes - they're how we learn!

Remember: Every programmer started by writing "Hello World!"
"""
