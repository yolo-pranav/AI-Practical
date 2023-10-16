import heapq

class State:
    def __init__(self, queens):
        self.queens = queens
        self.heuristic = self.calculate_heuristic()

    def calculate_heuristic(self):
        heuristic = 0
        for i in range(8):
            for j in range(i + 1, 8):
                if (
                    self.queens[i] == self.queens[j] or
                    abs(self.queens[i] - self.queens[j]) == j - i
                ):
                    heuristic += 1
        return heuristic

    def __lt__(self, other):
        return self.heuristic < other.heuristic

def is_goal(state):
    return state.heuristic == 0

def print_board(queens):
    for i in range(8):
        row = ["Q" if queens[i] == j else "." for j in range(8)]
        print(" ".join(row))

def solve_8queens():
    start_state = State([0, 0, 0, 0, 0, 0, 0, 0])
    open_set = [start_state]
    heapq.heapify(open_set)
    closed_set = set()

    while open_set:
        current_state = heapq.heappop(open_set)
        if is_goal(current_state):
            print("Solution found:")
            print_board(current_state.queens)
            break

        closed_set.add(tuple(current_state.queens))

        for i in range(8):
            for j in range(8):
                if i != j:
                    new_queens = current_state.queens[:]
                    new_queens[i] = j
                    neighbor = State(new_queens)

                    if tuple(neighbor.queens) not in closed_set:
                        heapq.heappush(open_set, neighbor)

if __name__ == "__main__":
    solve_8queens()