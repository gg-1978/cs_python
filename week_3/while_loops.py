'''
# declare a variable to count the number of iterations
iterations = 0

# display ready message
print("Starting iterations...")

# display the current count
while iterations < 10:

    # update the iteration count
    iterations += 1

# display completion message
print(f"Completed {iterations} iterations!")
'''
'''
print("How many apples should I remove?")
apples = int(input())
start_num = 0

while start_num < apples:
    print("Removed apple")
    start_num += 1

print(f"You removed {apples} apples!")
'''
'''
print("How many obstacles should I avoid? ")
# passes the value input value to the obstacle variable
obstacles = int(input())
current = 0

while current < obstacles:
    # the iteration line comes before the print line, so that current isn't 0!
    current += 1
    # prints a running count of obstacles avoided
    print(f"Avoiding...Done! {current} obstacles avoided!")

print(f"Completed. Total obstacles avoided: {obstacles}")
'''

print("How many bars should be charged?")
bars = int(input())
bars_charged = 0

while bars_charged < bars:
    print("Charging: ")


'''
# calculating the first 100 numbers
number = 0
running_tot = 0
while number < 100:
    number += 1
    running_tot = running_tot + number

print(f"The total of the number to 100 is {running_tot}.")
'''
