'''
# prints a robot face 1o times
for count in range(0, 100, 10):
    print("##########")
    print("#        #")
    print("# 0    0 #")
    print("#        #")
    print("#   []   #")
    print("#        #")
    print("#  ____  #")
    print("#        #")
    print("##########")
'''
'''
print("How many robots should I print?")
robots = int(input())


for count in range(0, robots, 1):
    print("##########")
    print("#        #")
    print("# 0    0 #")
    print("#        #")
    print("#   []   #")
    print("#        #")
    print("#  ____  #")
    print("#        #")
    print("##########")
'''

print("How far from the target are you?")
distance = int(input())

for count in range(distance, 0, -1):
    print(f"{count} steps remaining!")

print("Target reached!")

