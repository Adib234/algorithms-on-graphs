# Uses python3
n, m = map(int, input().split())
edgeList = []

for i in range(m):
    u, v, w = map(int, input().split())
    edgeList.append([u, v, w])

dist = [10000000 for i in range(n)]
dist[0] = 0
negativeCycle = False
for i in range(n-1):
    for u in edgeList:
        a, b, w = u
        if dist[a-1] + w < dist[b-1]:
            dist[b-1] = dist[a-1]+w
for j in edgeList:
    a, b, w = j
    if dist[a-1] + w < dist[b-1]:
        dist[b-1] = dist[a-1]+w
        negativeCycle = True
        break
print('1' if negativeCycle else '0')
