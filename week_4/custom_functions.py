
def listen():
    print("What did you hear?")
    sound = input().lower()
    print(f"\nThat was a loud {sound}!")

def identify():
    print("What lies before us?")
    danger = input().lower()
    if danger == "a large boulder":
        print("It's time to run!")
    else:
        print("We will be fine.")
    return danger

def escape_by(plan):
    if plan == "jumping over":
        print(f"We cannot escape that way! The {danger} is too big!")
    elif plan == "running around":
        print(f"We cannot escape that way! The {danger} is moving too fast!")
    elif plan == "cross bridge ahead":
        print("That might just work! Let's go!")
    else:
        print(f"We cannot escape that way. The {danger} is in the way!")

def cross_bridge(distance):
    if distance <= 5:
        print("\nCrossed step" * distance)
        print("We must keep going!")
    else:
        print("\nCrossed step" * 5)
        print("The bridge is collapsing")

def climb_ladder(steps_crossed, steps_remaining):
    if steps_crossed < steps_remaining:
        print("Still some way to go!")
    else:
        print("Almost there")
    return steps_remaining - steps_crossed


def display_ladder(steps):
    print("| |")
    for step in range(0, steps, 1):
        print("***")
        print("| |")

def create_ladder():
    print("How many steps remain?")
    # steps = int(input())
    print(f"There are {steps} steps remaining")
    display_ladder(steps)


listen()
# this passes the user input into the variable danger
# to allow it to be used by the function escape_by
danger = identify()
escape_by("jumping over")
escape_by("running around")
escape_by("cross bridge ahead")
cross_bridge(3)
cross_bridge(6)
# climb_ladder(9, 12)
steps = climb_ladder(9, 12)
create_ladder()
