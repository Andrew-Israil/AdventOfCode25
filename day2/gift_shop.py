import sys

def is_invalid_part1(st):

    if len(st) % 2 != 0:
        return False

    mid_id = len(st)//2
    if(st[:mid_id] == st[mid_id:]):
        return True

    return False

def is_invalid_part2(st):
    st_len = len(st)

    for sub_len in range(1, st_len // 2 + 1):
        occurrences = st_len // sub_len
        if(st_len % sub_len == 0):
            sub_str = st[:sub_len]
            if(st.count(sub_str) == occurrences):
                return True
            
    return False

with open(sys.argv[1], "r") as f:
    ranges = f.read().strip().split(",")

invalid_ids = 0

for r in ranges:
    start, end = map(int, r.split("-"))
    for id in range(start, end + 1):
        id_str = str(id)
        if(is_invalid_part2(id_str)):
            invalid_ids += id

print(f"sum of invalid ids is {invalid_ids}")
