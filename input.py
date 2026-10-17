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

# name = input("What is your name? ")
# age = input("How old are you? ")
# height = input("How tall are you (in metres)? ")
# weight = input("How much do you weight (in kg)? ")

# height_sq = float(height) * float(height)
# bmi = int(weight) / (height_sq)

# print(f"{name} you are {age} years old and your bmi is {int(bmi)}!")

# with open(.../data/info.txt, "w") as file:
#    file.write(f"Name: {name}\n")
#    file.write(f"Age: {age}\n")
#    file.write(f"Height: {height}\n")
#    file.write(f"Weight: {weight}\n")
#    file.write(f"BMI: {bmi}\n")

lives = int(input("Please enter the no. of lives: "))
energy = int(input("Please enter the enrgy level: "))
shield = int(input("Please enter the shield level: "))

lives_icon = chr(10084)
energy_icon = chr(10070)
shield_icon = chr(10026)

print("Health has been set.\n")
print(f"Lives: ", lives_icon * lives)
print(f"Energy: ", energy_icon * energy)
print(f"Shield: ", shield_icon * shield)


