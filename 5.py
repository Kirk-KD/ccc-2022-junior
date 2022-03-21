import sys
input = lambda: sys.stdin.readline().strip()

N = int(input())
T = int(input())
trees = []
for _ in range(T):
    s = input().split()
    trees.append((int(s[0]) - 1, int(s[1]) - 1))

def is_too_large(o_row, o_col, row, col):
    if row >= N or col >= N:
        return True, None

    for t_row, t_col in trees:
        if o_row <= t_row and o_col <= t_col and row >= t_row and col >= t_col:
            return True, (t_row, t_col)
    
    return False, None

largest = 0

row = 0
col = 0

while row < N:
    while col < N:
        if N - col <= largest or N - row <= largest:
            break

        size = 0

        while True:
            too_large, tree_hit = is_too_large(row, col, row + size, col + size)
            if too_large:
                if tree_hit:
                    t_row, t_col = tree_hit
                    col = t_col

                break
                
            size += 1
        
        if size > largest:
            largest = size

        col += 1
    
    row += 1
    col = 0

print(largest)
