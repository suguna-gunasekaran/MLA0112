graph = {
    1: [2, 7],
    2: [3, 6],
    3: [4, 5],
    4: [],
    5: [],
    6: [],
    7: [8, 10],
    8: [9],
    9: [],
    10: []
}

# BFS
queue = [1]
visited = {1}

print("BFS:", end=" ")
while queue:
    node = queue.pop(0)
    print(node, end=" ")

    for n in graph[node]:
        if n not in visited:
            visited.add(n)
            queue.append(n)

# DFS
visited = set()

def dfs(v):
    visited.add(v)
    print(v, end=" ")
    for n in graph[v]:
        if n not in visited:
            dfs(n)

print("\nDFS:", end=" ")
dfs(1)
