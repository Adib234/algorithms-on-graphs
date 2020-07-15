# Uses python3
n, m = map(int, input().split())
edgeList = []

for i in range(m):
    u, v, w = map(int, input().split())
    edgeList.append([u, v, w])
x = int(input())
dist = [10**19 for i in range(n)]
dist[x-1] = 0

output = [None for i in range(n)]
for i in range(n-1):
    for u in edgeList:
        a, b, w = u
        if dist[a-1] + w < dist[b-1]:
            dist[b-1] = dist[a-1]+w
for j in edgeList:
    a, b, w = j
    if dist[a-1] + w < dist[b-1]:
        dist[b-1] = dist[a-1]+w
        output[b-1] = "-"
dist[x-1] = 0
for i in range(len(output)):
    if output[i] == None and dist[i] != 10**19:
        output[i] = dist[i]
    elif output[i] == None and dist[i] == 10**19:
        output[i] = "*"

for i in range(len(output)):
    print(output[i])
