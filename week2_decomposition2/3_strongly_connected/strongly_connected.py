# Uses python3

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


overall = {}
keys = []
for i in range(n):
    path = (dfs(adj, i+1))
    path = ''.join([str(x) for x in path])
    if path not in overall:
        keys.append(path)
        overall[path] = 1

print(len(overall))
