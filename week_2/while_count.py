
print("How many obstacles should I avoid? ")
obstacles = int(input())

obstacles_avoid = 0

while obstacles_avoid < obstacles:
    print("Avoiding...", end="")
    obstacles_avoid += 1
    print(f"Done! {obstacles_avoid} obstacles avoided...")
