from collections import deque

start = (0, 0)
goal = 8

visited = set()
queue = deque([(start, [])])

while queue:
    (a, b), path = queue.popleft()

    if a == goal or b == goal:
        print("Solution Found")
        print(path + [(a, b)])
        break

    if (a, b) in visited:
        continue

    visited.add((a, b))

    next_states = []

    next_states.append((11, b))
    next_states.append((a, 9))
    next_states.append((0, b))
    next_states.append((a, 0))

    pour = min(a, 9 - b)
    next_states.append((a - pour, b + pour))

    pour = min(b, 11 - a)
    next_states.append((a + pour, b - pour))

    for state in next_states:
        if state not in visited:
            queue.append((state, path + [(a, b)]))
