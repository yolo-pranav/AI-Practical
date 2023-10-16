from collections import deque

def water_jug_bfs(capacity_a, capacity_b, target):
    visited = set()
    queue = deque()
    initial_state = (0, 0)  # Initial state of the jugs (0 liters in both jugs)
    queue.append(initial_state)

    while queue:
        current_state = queue.popleft()
        a, b = current_state

        print("Current state: ({}, {})".format(a, b))

        if a == target or b == target:
            print("Goal state reached: ({}, {})".format(a, b))
            return

        if (a, b) in visited:
            continue

        visited.add((a, b))

        # Fill Jug A
        if a < capacity_a:
            queue.append((capacity_a, b))

        # Fill Jug B
        if b < capacity_b:
            queue.append((a, capacity_b))

        # Empty Jug A
        if a > 0:
            queue.append((0, b))

        # Empty Jug B
        if b > 0:
            queue.append((a, 0))

        # Pour from Jug A to Jug B
        if a > 0 and b < capacity_b:
            pour = min(a, capacity_b - b)
            queue.append((a - pour, b + pour))

        # Pour from Jug B to Jug A
        if b > 0 and a < capacity_a:
            pour = min(b, capacity_a - a)
            queue.append((a + pour, b - pour))

    print("Goal state not reachable")

# Example usage
capacity_a = 4
capacity_b = 3
target = 2
water_jug_bfs(capacity_a, capacity_b, target)