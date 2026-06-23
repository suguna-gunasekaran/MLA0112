import math

# Tree structure from your notes
# Terminal nodes: H=4, I=2, J=5, K=7, L=0, M=1, N=6, O=4
tree = {
    'A': ['B', 'C'], # MAX
    'B': ['D', 'E'], # MIN
    'C': ['F', 'G'], # MIN
    'D': ['H', 'I'], # MAX
    'E': ['J', 'K'], # MAX
    'F': ['L', 'M'], # MAX
    'G': ['N', 'O'], # MAX
    'H': 4, 'I': 2, 'J': 5, 'K': 7,
    'L': 0, 'M': 1, 'N': 6, 'O': 4
}

def minimax(node, is_maximizing):
    # If it's a terminal node, return value
    if isinstance(tree[node], int):
        return tree[node]
    
    if is_maximizing:
        best_val = -math.inf
        for child in tree[node]:
            val = minimax(child, False)
            best_val = max(best_val, val)
        print(f"MAX {node} = {best_val}")
        return best_val
    else:
        best_val = math.inf
        for child in tree[node]:
            val = minimax(child, True)
            best_val = min(best_val, val)
        print(f"MIN {node} = {best_val}")
        return best_val

# Run from root A, MAX starts first
result = minimax('A', True)
print(f"\nOptimal value at root A: {result}") # Should be 2
