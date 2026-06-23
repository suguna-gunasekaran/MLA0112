import heapq

def greedy_best_first_search(graph, heuristics, start, goal, graph_name):
    print(f"\n{'='*60}")
    print(f"GBFS - {graph_name}")
    print(f"Start: {start}, Goal: {goal}")
    print(f"{'='*60}")
    print(f"{'Step':<6} {'Node':<6} {'h(n)':<6} {'Path':<25} {'Queue'}")
    print(f"{'-'*60}")
    
    # Priority queue: (h, path, node)
    pq = [(heuristics[start], [start], start)]
    visited = set()
    step = 1
    
    while pq:
        h, path, node = heapq.heappop(pq)
        
        if node in visited:
            continue
        visited.add(node)
        
        queue_state = [f"{item[1][-1]}({item[0]})" for item in pq]
        print(f"{step:<6} {node:<6} {h:<6} {' -> '.join(path):<25} {queue_state}")
        
        if node == goal:
            print(f"\nGOAL REACHED!")
            print(f"GBFS Path: {' -> '.join(path)}")
            return path
        
        # Expand neighbors - GBFS picks lowest h(n) only
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                new_path = path + [neighbor]
                heapq.heappush(pq, (heuristics[neighbor], new_path, neighbor))
        
        step += 1
    
    print("Goal not reachable")
    return None

# ======================================================
# GRAPH 1: Top graph in notes - A to G
# ======================================================
graph1 = {
    'A': ['D', 'C', 'B'],
    'D': ['F'],
    'C': ['F'],
    'B': ['E'],
    'F': ['G'],
    'E': ['H'],
    'H': ['G'],
    'G': []
}
heuristics1 = {
    'A': 40, 'B': 32, 'C': 25, 'D': 35, 
    'E': 19, 'F': 17, 'H': 10, 'G': 0
}

# ======================================================
# GRAPH 2: Middle graph in notes - A to G 
# ======================================================
graph2 = {
    'A': ['D', 'C', 'B'],
    'D': ['F'],
    'C': ['F'],
    'B': ['E'],
    'F': ['G'],
    'E': ['H'],
    'H': ['G'],
    'G': []
}
heuristics2 = {
    'A': 40, 'B': 32, 'C': 25, 'D': 35, 
    'E': 19, 'F': 17, 'H': 10, 'G': 0
}

# ======================================================
# GRAPH 3: Bottom graph in notes - P to S
# ======================================================
graph3 = {
    'P': ['R', 'A', 'C'],
    'R': ['E'],
    'A': ['M'],
    'C': ['M', 'U'],
    'M': ['U', 'L'],
    'U': ['R', 'E', 'S', 'L'],
    'E': ['S'],
    'L': ['N'],
    'N': ['S'],
    'S': []
}
heuristics3 = {
    'P': 10, 'R': 8, 'A': 1, 'C': 6, 
    'M': 9, 'U': 4, 'E': 3, 'L': 9, 
    'N': 6, 'S': 0
}

# ======================================================
# RUN ALL 3 GBFS EXAMPLES
# ======================================================
if __name__ == "__main__":
    # Graph 1 & 2 are same structure from your notes
    greedy_best_first_search(graph1, heuristics1, 'A', 'G', "GRAPH 1: A to G")
    
    greedy_best_first_search(graph2, heuristics2, 'A', 'G', "GRAPH 2: A to G")
    
    # Graph 3: P to S
    greedy_best_first_search(graph3, heuristics3, 'P', 'S', "GRAPH 3: P to S")
