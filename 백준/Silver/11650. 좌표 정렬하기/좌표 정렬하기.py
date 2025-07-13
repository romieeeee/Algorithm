n = int(input()) 

graph = []
for _ in range (n):
    graph.append(list(input().split()))

graph.sort(key = lambda x:(int(x[0]), int(x[1])))

for member in graph:
    print(' '.join(member))