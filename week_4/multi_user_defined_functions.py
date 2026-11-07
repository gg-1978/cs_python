
# def display_box(name):
#     message = f"* Hello {name} *"
#     print("*" * len(message))
#     print(message)
#     print("*" * len(message))

# def greet_user():
#     print("Please enter your name")
#     name = input()
#     display_box(name)

# greet_user()

def get_name():
    print("Please enter your name")
    name = input()
    return name

print("Retrieved name:", get_name())
