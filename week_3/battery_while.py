
print("How many bars should be charged? ")
bar_to_charge = int(input())

bars = 0

battery = ""

while bars < bar_to_charge:
    bars += 1
    battery = battery + "*"
    print(f"Charging: {battery}")

print("The battery is full")
