import sys

with open(sys.argv[1], "r") as f:
    lines = f.read().strip().split("\n")


grid = [list(line) for line in lines]
rows = len(grid)
cols = len(grid[0])
max_occupied_neighbors = 3
accessible_grid_count = 0

def get_occupied_neighbors(r,l):
    occ = []
    start_row = r-1 if r > 0 else 0
    start_col = l-1 if l > 0 else 0
    end_row = r+1 if r < rows-1 else rows-1
    end_col = l+1 if l < cols-1 else cols-1

    for row in range(start_row,end_row+1):
        for col in range(start_col,end_col+1):
            if((row,col) != (r,l) and grid[row][col] == "@"):
                pos = (row,col)
                occ.append(pos)

    return occ

def remove_accessible():
    removed = 0
    for row in range(rows):
        for col in range(cols):
            if(grid[row][col] == "@"):
                occ_nei = get_occupied_neighbors(row,col)
                if(len(occ_nei) <= max_occupied_neighbors):
                    removed += 1
                    grid[row][col] = "."    
    return removed

######## for Part 1 #########
# for row in range(rows):
#     for col in range(cols):
#         if(grid[row][col] == "@"):
#             occ_nei = get_occupied_neighbors(row,col)
#             if(len(occ_nei) <= max_occupied_neighbors):
#                 accessible_grid_count += 1
##############################    

total_removed = 0      
while(True):
    removed = remove_accessible()
    if(removed > 0):
        total_removed += removed
    else:
        break           

############# for Part 1 #############################
#print(f"Accessible psoitions count = {accessible_grid_count}")

print(f"Total removed rolls = {total_removed}")
