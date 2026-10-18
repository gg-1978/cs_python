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



# lives = int(input("Please enter the no. of lives: "))
# energy = int(input("Please enter the enrgy level: "))
# shield = int(input("Please enter the shield level: "))

# lives_icon = chr(10084)
# energy_icon = chr(10070)
# shield_icon = chr(10026)

# print("Health has been set.\n")
# print(f"Lives: ", lives_icon * lives)
# print(f"Energy: ", energy_icon * energy)
# print(f"Shield: ", shield_icon * shield)

name = input("What is your name? ")
age = input("How old are you? ")
height = input("How tall are you (in metres)? ")
weight = input("How much do you weight (in kg)? ")

# .strip means spaces are removed from either end
# .lower means that the file name created in line 53 will be the same format as other file
file_name = name.strip().lower()

height_sq = float(height) * float(height)
bmi = int(weight) / (height_sq)
write_bmi = int(bmi)
weight = round(float(weight), 1)

print(f"{name} you are {age} years old and your bmi is {int(bmi)}!")

with open(f"/home/ubuntu/cs_python/cs_python/data/{file_name}.txt", "w") as file:
   file.write(f"Name: {name}\n")
   file.write(f"Age: {age} yrs\n")
   file.write(f"Height: {height}m\n")
   file.write(f"Weight: {weight}kg\n")
   file.write(f"BMI: {write_bmi}\n")
