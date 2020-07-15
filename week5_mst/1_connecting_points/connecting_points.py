# Uses python3
# Got help for this one lol, from Tyler Tian

import math


def dist(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


points = [tuple(int(i) for i in input().split()) for _ in range(int(input()))]
# print(points)
# Total edge weight
w = 0
# Dict of points -> min distance to the point
dists = {}
# Add all points except for one into the queue
ipts = iter(points)
# print(ipts)
pt = next(ipts)  # skip first entry
# print(pt)
for p in ipts:
    dists[p] = dist(p, pt)
# print(dists)
# Prim's algorithm
while dists:
    # Find point with minimum distance
    d = 100000000
    p = None
    for k, v in dists.items():
        if v < d:
            d = v
            p = k
    dists.pop(p)
    w += d
    # print(p)
    # print(d)
    # Update distances
    for k in dists.keys():
        d = dist(p, k)
        if d < dists[k]:
            dists[k] = d
    # print(dists)


print("{0:.9f}".format(w))
# import math
# import heapq

# n = int(input())
# edgeList = []

# for i in range(n):
#     u, v = map(int, input().split())
#     edgeList.append([u, v])

# h = []
# heapq.heappush(h, edgeList[0])

# visited = set()


# def findAllDistance(a, x, visited):
#     dist = [10000000 for i in range(len(x))]
#     for i in range(len(x)):
#         if x[i] != a and x.index(x[i]) not in visited:
#             dist[i] = math.sqrt((a[0]-x[i][0])**2+(a[1]-x[i][1])**2)
#     return dist


# total = 0
# while len(h) != 0:
#     print(h)
#     current = heapq.heappop(h)
#     if edgeList.index(current) not in visited:
#         shortest = findAllDistance(current, edgeList, visited)
#         total += min(shortest) if min(shortest) != 10000000 else 0
#         print(total)
#         heapq.heappush(h, edgeList[shortest.index(min(shortest))])
#     visited.add(edgeList.index(current))

# print(total)


# # print("{0:.9f}".format())
