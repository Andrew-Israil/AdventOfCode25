import sys


with open(sys.argv[1], "r") as f:
    rotations = list(map(str.strip, f.readlines()))

dial = 50
last_step = 99
total_steps = 100
zeros_end_rotation = 0
zeros_mid_rotation = 0

for rotation in rotations:
    direction = rotation[0]
    clicks_num = int(rotation[1:])

    remaining_right_steps = last_step - dial

    if(clicks_num > total_steps):
        zeros_mid_rotation += clicks_num // total_steps
        clicks_num = clicks_num % total_steps

    if(direction == "R"):
        if(clicks_num > remaining_right_steps):
            dial = clicks_num - remaining_right_steps - 1
            if(dial != 0):
                zeros_mid_rotation += 1
        else:
            dial = dial + clicks_num

    else:
        if(clicks_num > dial):
            if(dial != 0):
                zeros_mid_rotation += 1
            dial = last_step - (clicks_num - dial - 1)
        else:
            dial = dial - clicks_num
        
    if dial == 0:
        zeros_end_rotation += 1

print(f"zeros at the end of a rotation = {zeros_end_rotation}")
print(f"zeros amid a rotation = {zeros_mid_rotation}")
print(f"total zeros = {zeros_end_rotation + zeros_mid_rotation}")
