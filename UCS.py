import heapq

def uniform_cost_search(graph, start, goal):
    # Priority queue: (cost, path, node)
    pq = [(0, [start], start)]
    visited = set()
    
    while pq:
        cost, path, node = heapq.heappop(pq)
        
        # If we reached goal, return
        if node == goal:
            return cost, path
            
        if node in visited:
            continue
        visited.add(node)
        
        # Explore neighbors
        for neighbor, edge_cost in graph.get(node, []):
            if neighbor not in visited:
                new_cost = cost + edge_cost
                new_path = path + [neighbor]
                heapq.heappush(pq, (new_cost, new_path, neighbor))
                print(f"Enqueue: {new_path} with cost {new_cost}")
    
    return float('inf'), []

# Graph from your diagram
graph = {
    'S': [('A', 1), ('G', 12)],
    'A': [('B', 3), ('C', 1)],
    'B': [('D', 3)],
    'C': [('D', 1), ('G', 2)],
    'D': [('G', 3)]
}

cost, path = uniform_cost_search(graph, 'S', 'G')
print(f"\nOptimal path: {' -> '.join(path)}")
print(f"Total cost: {cost}")
