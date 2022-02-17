from ast import parse
import sys
input = lambda: sys.stdin.readline().strip()

instructions = input()
parsed = [["", "", ""]]

i = 0
prev = ""
while i < len(instructions):
    if instructions[i].isalpha():
        if prev.isnumeric():
            parsed.append(["", "", ""])
        parsed[-1][0] += instructions[i]
    elif instructions[i] == '+':
        parsed[-1][1] = "tighten"
    elif instructions[i] == '-':
        parsed[-1][1] = "loosen"
    else:
        parsed[-1][2] += instructions[i]
    prev = instructions[i]

    i += 1

for p in parsed:
    print(' '.join(p))
