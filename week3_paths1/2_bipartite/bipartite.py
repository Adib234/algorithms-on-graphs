#Uses python3
from queue import Queue

n, m = map(int, input().split())
adj = [[] for i in range(n)]

for i in range(m):
    u, v = map(int, input().split())
    adj[u-1].append(v)
    adj[v-1].append(u)

q = Queue()
q.put(0)
visited = set()
visited.add(1)
color = [-1 for i in range(len(adj))]
color[0]=0
# 0 for red 1 for blue
bipartite=True
while q.empty() == False:
    visiting = q.get()
    for i in adj[visiting]: 
        check=color[visiting]
        if i not in visited and color[i-1]!=check:
            q.put(i-1)
            visited.add(i)
            color[i-1]=0 if check==1 else 1
        elif color[i-1]==check:
            bipartite=False
            break
#print(color)
print(1 if bipartite else 0)