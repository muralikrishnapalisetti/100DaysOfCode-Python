import random

# Define the characters for password generation manually
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Welcome message
print("Welcome to the Password Generator!")

# User input for number of letters, symbols, and numbers
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# List to store the password characters
password_list = []

# Adding random letters to the password list
for _ in range(nr_letters):
    password_list.append(random.choice(letters))

# Adding random symbols to the password list
for _ in range(nr_symbols):
    password_list.append(random.choice(symbols))

# Adding random numbers to the password list
for _ in range(nr_numbers):
    password_list.append(random.choice(numbers))

# Shuffle the password list
random.shuffle(password_list)

# Join the password list into a string
password = "".join(password_list)

# Display the generated password
print(f"Your generated password is: {password}")
