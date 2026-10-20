
book_type = input("Enter type of book: ").lower()

print(f"I like {book_type} books!")

print("Finished reading book!")

activity = input("Enter type of activity: ").lower()

if activity == "calculate":
    print("Performing calculations...")
else:
    print("Performing activity...")

print("Activity completed!")
