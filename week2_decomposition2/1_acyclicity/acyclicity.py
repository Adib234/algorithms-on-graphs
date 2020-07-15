# Uses python3

n, m = map(int, input().split())
adj = [[] for i in range(n)]

for i in range(m):
    u, v = map(int, input().split())
    adj[u-1].append(v)


def dfs(adj, i):
    visited = set()
    visited.add(i)
    stack = [i-1]
    path = [i]
    while stack:
        visiting = stack.pop()
        for i in adj[visiting]:
            if i not in visited:
                visited.add(i)
                stack.append(i-1)
                path.append(i)
    return sorted(path)


overall = []
cycle = False
for i in range(n):
    #print(dfs(adj, i+1))
    if dfs(adj, i+1) not in overall:
        overall.append(dfs(adj, i+1))
    else:
        cycle = True
        break
# print(overall)
print('1' if cycle else '0')
