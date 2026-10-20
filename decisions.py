# check whether first number is bigger than second number
# assume first_number and second_number are existing variables

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
