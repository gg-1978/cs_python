'''
print("Program Started!")
print("Please enter a standard character:")

letter = input()

if len(letter) == 1:
    value = int(ord(letter))
    print(f"The ASCII code for {letter} is: {value}.")
else:
    print("Error. Program ended!")
'''

print("Program Started!")
print("Please enter an ASCII code:")

code = int(input())

if code in range(32, 126):
    ascii = chr(code)
    print(f"The character represented by the ASCII code {code} is: {ascii}.")
else:
    print("Error. Program ended!")




