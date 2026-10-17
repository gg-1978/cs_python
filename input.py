# ask user to enter their name

# print("What is your name?")
# name = input()
# print(f"Nice to meet you, {name}.")

# a way to combine the first 2 lines

# name = input("What is your name? ")
# print(f"Nice to meet you, {name}.")

# eyes = input("Enter a symbol for eyes: ")

# print("##########")
# print(f"#  {eyes}  {eyes}  #")
# print("#  ____  #")
# print("##########")

# whole_number = int(input("Enter your age: "))

# user_age = whole_number
# print(f"Your age is {user_age}.")

# decimal_number = float(input())

name = input("What is your name? ")
age = input("How old are you? ")
height = input("How tall are you (in metres)? ")
weight = input("How much do you weight (in kg)? ")

height_sq = float(height) * float(height)
bmi = int(weight) / (height_sq)


print(f"{name} you are {age} years old and your bmi is {int(bmi)}!")





