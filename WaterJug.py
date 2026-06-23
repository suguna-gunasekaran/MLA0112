from collections import deque

# Capacities of jugs
A_CAPACITY = 4
B_CAPACITY = 3

# Goal state
GOAL = (2, 0)

def get_next_states(a, b):
    states = []

    # Fill A
    states.append((A_CAPACITY, b))

    # Fill B
    states.append((a, B_CAPACITY))

    # Empty A
    states.append((0, b))

    # Empty B
    states.append((a, 0))

    # Transfer A -> B
    transfer = min(a, B_CAPACITY - b)
    states.append((a - transfer, b + transfer))

    # Transfer B -> A
    transfer = min(b, A_CAPACITY - a)
    states.append((a + transfer, b - transfer))

    return states

def water_jug():
    start = (0, 0)

    queue = deque([(start, [start])])
    visited = set()

    while queue:
        (a, b), path = queue.popleft()

        if (a, b) == GOAL:
            print("Solution Path:")
            for state in path:
                print(state)
            return

        if (a, b) in visited:
            continue

        visited.add((a, b))

        for next_state in get_next_states(a, b):
            if next_state not in visited:
                queue.append((next_state, path + [next_state]))

    print("No solution found")

water_jug()
