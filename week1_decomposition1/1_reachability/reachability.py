# python3
n, m = map(int, input().split())
adj = [[] for i in range(n)]

for i in range(m):
    u, v = map(int, input().split())
    adj[u-1].append(v)
    adj[v-1].append(u)
x, y = map(int, input().split())
visited = set()
stack = []
visited.add(x)
stack.append(x-1)
found = False
while stack:
    visiting = stack.pop()
    for i in (adj[visiting]):
        if i == y:
            found = True
            break
        if i not in visited:
            visited.add(i)
            stack.append(i-1)

print('1' if found else '0')
