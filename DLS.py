def dls(graph, start, goal, limit, path=None):
    if path is None:
        path = [start]
    
    print(f"Visit: {start}, Depth: {len(path)-1}, Limit: {limit}, Path: {path}")
    
    if start == goal:
        return path
    if limit <= 0:
        return None
    
    for neighbor in graph[start]: # Left then right
        result = dls(graph, neighbor, goal, limit-1, path + [neighbor])
        if result:
            return result
    return None

print("\n=== Depth Limited Search with limit=2 ===")
dls_path = dls(graph1, 'A', 'I', 2)
print(f"\nDLS Result: {dls_path}") # None - I is at depth 3

print("\n=== Depth Limited Search with limit=3 ===")
dls_path = dls(graph1, 'A', 'I', 3)
print(f"\nDLS Path to I: {' -> '.join(dls_path)}")
