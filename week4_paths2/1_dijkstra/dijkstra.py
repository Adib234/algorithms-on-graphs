# Uses python3

from queue import Queue
import heapq
n, m = map(int, input().split())
adj = [[] for i in range(n)]

for i in range(m):
    u, v, w = map(int, input().split())
    adj[u-1].append([v, w])

x, y = map(int, input().split())
x, y = x-1, y-1

visited = set()

dist = [float('inf') for i in range(n)]
dist[x] = 0

h = []
heapq.heappush(h, [dist[x], x])

while len(h) != 0:
    # print(h)
    current = heapq.heappop(h)
    visiting = current[1]
    if visiting+1 not in visited:
        for i in adj[visiting]:
            u, v = i
            # flipped because weight is more important
            dist[u-1] = dist[visiting]+v if dist[visiting] + \
                v < dist[u-1] else dist[u-1]
            heapq.heappush(h, [dist[u-1], u-1])
    visited.add(visiting+1)
    # print(h)
# print(dist)
if dist[y] != float('inf'):
    print(dist[y])
else:
    print(-1)
