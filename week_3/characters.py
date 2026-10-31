'''
print("Please enter a word")

user_word = input()

for position in range(0, len(user_word), 1):
    print(user_word, position)
'''


word = str(input("What word do you see?: "))

print("Displaying index positions of each character")

for index in range(0, len(word), 1):
    print(f"Index {index}: {word[index]}")

