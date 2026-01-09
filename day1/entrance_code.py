import sys


with open(sys.argv[1], "r") as f:
    rotations = list(map(str.strip, f.readlines()))

dial = 50
last_step = 99
total_steps = 100
zeros = 0

for rotation in rotations:
    direction = rotation[0]
    clicks_num = int(rotation[1:])

    print(f"dial = {dial}")
    print(f"operation = {rotation}")

    remaining_right_steps = last_step - dial

    if(clicks_num > total_steps):
        clicks_num = clicks_num % total_steps

    if(direction == "R"):
        if(clicks_num > remaining_right_steps):
            dial = clicks_num - remaining_right_steps - 1
        else:
            dial = dial + clicks_num

    else:
        if(clicks_num > dial):
            dial = last_step - (clicks_num - dial - 1)
        else:
            dial = dial - clicks_num
        
    print(f"dial = {dial}")
    if dial == 0:
        zeros += 1

print(f"zeros = {zeros}")
