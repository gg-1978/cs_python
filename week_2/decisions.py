# check whether first number is bigger than second number
# assume first_number and second_number are existing variables
'''
# Number

first_num = input("Enter first number: ")
second_num = input("Enter second number: ")

if first_num > second_num:
    print("First number is bigger")
elif first_num < second_num:
    print("First number is smaller")
else:
    print("Both numbers are the same")

# this line will print regardless of outcome as it is outside of
# the if statement
print("Done!")

# Entity

entity = input("Enter entity type: ").lower()

if entity == "human":
    print("You are a human!")
elif entity == "robot":
    print("You are a robot!")
elif entity == "animal":
    print("You are an animal!")
else:
    print("I do not know what you are!")

print("Analysis complete")

'''
# Direction
'''
mapping = True

while mapping == True:
    direction = input("Enter a direction (Up, Down, Left or Right): ").lower()

    if direction == "up":
        print("I am moving in an upward direction!\n")
        end = input("Have you finished your journey? (Y/N): ").lower()
        if end == "y" or end == "yes":
            mapping = False
    elif direction == "down":
        print("I am moving in a downward direction!\n")
        end = input("Have you finished your journey? (Y/N): ").lower()
        if end == "y" or end == "yes":
            mapping = False
    elif direction == "left":
        print("I am moving to the left!\n")
        end = input("Have you finished your journey? (Y/N): ").lower()
        if end == "y" or end == "yes":
            mapping = False
    elif direction =="right":
        print("I am moving to the right!\n")
        end = input("Have you finished your journey? (Y/N): ").lower()
        if end == "y" or end == "yes":
            mapping = False
    else:
        print("Error. Please enter a valid direction!\n")
'''

# Modulo

number = input("Enter a whole number: ")

modulo = int(number) % 2

if modulo == 0:
    print(f"The number {number} is an even number!")
elif modulo == 1:
    print(f"The number {number} is an odd number!")
else:
    print("Error!")

