import sys

def get_max_jolt(bank):
    first_digit = max(bank[:-1])
    largest_index = bank.index(first_digit)
    second_digit = max(bank[largest_index+1:])
    return (first_digit * 10) + second_digit

def get_next_max_val_index(l, val, ind):
    for i in range(ind+1,len(l)):
        if(l[i] == val):
            index = i
            break
    return index


def get_max_jolt_part2(bank):
    # while(len(bank)<12):
    #     bank.remove(min(bank))
    remaining = 12
    jolt = 0
    largest_index = -1
    while(remaining > 0):
        search_end = len(bank) - remaining
        largest_val = max(bank[largest_index+1:search_end+1])
        #largest_index = bank.index(largest_val)
        largest_index = get_next_max_val_index(bank, largest_val, largest_index)
        jolt += largest_val*(10**(remaining-1))
        remaining -= 1
    return jolt

with open(sys.argv[1], 'r') as f:
    banks = list(map(str.strip, f.readlines()))
    
max_jolt = 0

for bank in banks:
    batteries = []

    for battery in bank:
        batteries.append(int(battery))
    

    max_jolt += get_max_jolt_part2(batteries)

print(f"max jolt = {max_jolt}")