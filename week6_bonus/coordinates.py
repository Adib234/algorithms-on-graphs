# python3
# Uses python3
import math
from queue import Queue
import heapq

n, m = map(int, input().split())
adj = [[] for i in range(n)]
points = [list(int(i) for i in input().split()) for _ in range(n)]

for i in range(m):
    u, v, w = map(int, input().split())
    adj[u-1].append([v, w])

targets = int(input())
tar = [list(int(i)-1 for i in input().split()) for _ in range(targets)]


def eucliddist(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def astar(adj, points, x, y):
    heuristics = [eucliddist(points[y], points[i]) for i in range(len(points))]
    # print(heuristics)
    visited = set()

    dist = [float('inf') for i in range(n)]
    dist[x] = 0

    h = []
    heapq.heappush(h, [heuristics[x], x])

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
                heuristics[u-1] = dist[u-1]+v
                heapq.heappush(h, [heuristics[u-1], u-1])
        visited.add(visiting+1)
        # print(h)
    # print(dist)
    if dist[y] != float('inf'):
        return dist[y]
    else:
        return -1


final = []
for i in range(targets):
    final.append(astar(adj, points, tar[i][0], tar[i][1]))

for i in range(len(final)):
    print(final[i])
