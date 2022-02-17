import sys
input = lambda: sys.stdin.readline().strip()

N = int(input())
x = [(int(input()), int(input())) for _ in range(N)]
c = 0
for g, f in x:
    if g * 5 - f * 3 > 40:
        c += 1

print(c, end='')
if c == N:
    print('+')
