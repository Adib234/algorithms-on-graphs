# Uses python3
# fails last test case of 10000 edges and vertices
n, m = map(int, input().split())
adj = [[] for i in range(n)]

for i in range(m):
    u, v = map(int, input().split())
    adj[u-1].append(v)
stack = [1]
path = []
visited = set()
perm = set()


def checked(adj, visited, i):
    c = 0
    if len(adj[i]) == 0:
        return True
    for j in adj[i]:
        if j in visited:
            c += 1
        else:
            return False
    if c == len(adj[i]):
        return True


while stack or (len(path) != n):
    visiting = stack.pop() - 1
    for i in adj[visiting]:
        if i not in visited or i not in perm:
            stack.append(i)
            visited.add(i)
            # check if vertex if leaf or has children that have already been visited
            if len(adj[i-1]) == 0 or checked(adj, perm, i-1):
                path.append(i)
                perm.add(i)

    # checking if the parent vertex has children that have already been visited
    if visiting+1 not in visited and checked(adj, perm, visiting):
        visited.add(visiting+1)
        perm.add(visiting+1)
        path.append(visiting+1)
    # if we run into a dead end but there's still exploration left to do
    if len(path) != n and len(stack) == 0:
        for j in range(n):
            if j+1 not in visited:
                stack.append(j+1)
                break
for k in list(reversed(path)):
    print(k, end=' ')
