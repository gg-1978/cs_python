
def listen():
    print("What did you hear?")
    sound = input().lower()
    print(f"\nThat was a loud {sound}!")

def identify():
    print("What lies before us?")
    object = input().lower()
    if object == "a large boulder":
        print("It's time to run!")
    else:
        print("We will be fine.")

def escape_by(plan):
    if plan == "jumping over":
        print("We cannot escape that way! The boulder is too big!")
    elif plan == "running around":
        print("We cannot escape that way! The boulder is moving too fast!")
    elif plan == "cross bridge ahead":
        print("That might just work! Let's go!")
    else:
        print("We cannot escape that way. The boulder is in the way!")


listen()
identify()
escape_by("jumping over")
escape_by("running around")
escape_by("cross bridge ahead")
