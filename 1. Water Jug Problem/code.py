from collections import deque

class State:
    def __init__(self, jug_a, jug_b):
        self.jug_a = jug_a
        self.jug_b = jug_b

    def __eq__(self, other):
        return self.jug_a == other.jug_a and self.jug_b == other.jug_b

    def __hash__(self):
        return hash((self.jug_a, self.jug_b))

def is_valid_state(state, capacity_a, capacity_b):
    return 0 <= state.jug_a <= capacity_a and 0 <= state.jug_b <= capacity_b

def water_jug_bfs(capacity_a, capacity_b, target):
    initial_state = State(0, 0)
    visited = set()
    queue = deque()
    queue.append((initial_state, []))

    while queue:
        current_state, actions = queue.popleft()

        if current_state.jug_a == target or current_state.jug_b == target:
            actions.append(f"Reached target: {target}")
            return actions

        # Generate all possible next states
        next_states = []

        # Fill jug A
        next_states.append(State(capacity_a, current_state.jug_b))

        # Fill jug B
        next_states.append(State(current_state.jug_a, capacity_b))

        # Empty jug A
        next_states.append(State(0, current_state.jug_b))

        # Empty jug B
        next_states.append(State(current_state.jug_a, 0))

        # Pour from A to B
        pour_amount = min(current_state.jug_a, capacity_b - current_state.jug_b)
        next_states.append(State(current_state.jug_a - pour_amount, current_state.jug_b + pour_amount))

        # Pour from B to A
        pour_amount = min(current_state.jug_b, capacity_a - current_state.jug_a)
        next_states.append(State(current_state.jug_a + pour_amount, current_state.jug_b - pour_amount))

        for state in next_states:
            if is_valid_state(state, capacity_a, capacity_b) and state not in visited:
                visited.add(state)
                queue.append((state, actions + [f"Fill jug A: {state.jug_a}, jug B: {state.jug_b}"]))

    return None

capacity_a = 4
capacity_b = 3
target_volume = 2
result = water_jug_bfs(capacity_a, capacity_b, target_volume)

if result:
    for action in result:
        print(action)
else:
    print("Target volume cannot be achieved.")