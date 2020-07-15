# Uses python3

from queue import Queue

n, m = map(int, input().split())
adj = [[] for i in range(n)]

for i in range(m):
    u, v = map(int, input().split())
    adj[u-1].append(v)
    adj[v-1].append(u)
x, y = map(int, input().split())
x, y = x-1, y-1
q = Queue()
q.put(x)
visited = set()
visited.add(x+1)
dist = [len(adj) for i in range(len(adj))]
dist[x] = 0
while q.empty() == False:
    visiting = q.get()
    for i in adj[visiting]:
        if i not in visited:
            q.put(i-1)
            visited.add(i)
            dist[i-1] = dist[visiting]+1
# print(dist)
if dist[y] != len(adj):
    print(dist[y])
else:
    print(-1)
