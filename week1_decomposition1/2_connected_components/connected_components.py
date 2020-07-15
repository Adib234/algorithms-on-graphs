# Uses python3
n, m = map(int, input().split())
adj = [[] for i in range(n)]

for i in range(m):
    u, v = map(int, input().split())
    adj[u-1].append(v)
    adj[v-1].append(u)
stack = []
visited = set()
visited.add(1)
stack.append(0)
count = 0
while stack and len(visited) != n:
    visiting = stack.pop()
    for i in adj[visiting]:
        if i not in visited:
            visited.add(i)
            stack.append(i-1)

    if len(stack) == 0 and len(visited) != n:
        count += 1
        for j in range(len(adj)):
            if j+1 not in visited:
                stack.append(j)
                visited.add(j+1)
                break

print(count+1)
