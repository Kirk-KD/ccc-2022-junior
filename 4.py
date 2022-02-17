import sys
input = lambda: sys.stdin.readline().strip()

X = int(input())
same_group = [set(input().split()) for _ in range(X)]
Y = int(input())
diff_group = [set(input().split()) for _ in range(Y)]
G = int(input())
groups = [input().split() for _ in range(G)]

def pick_two(g):
    return [set([g[0], g[1]]), set([g[0], g[2]]), set([g[1], g[2]])]

violation = 0

for g in groups:
    two = pick_two(g)
    same_group_c = same_group.copy()
    for s in same_group_c:
        if s in two:
            same_group.remove(s)

    for t in two:
        if t in diff_group:
            diff_group.remove(t)

violation += min(len(same_group) + Y - len(diff_group), X + Y)
print(violation)
