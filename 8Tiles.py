from heapq import heappop, heappush

class PuzzleState:

    def __init__(self, puzzle, parent=None, move=""):
        self.puzzle = puzzle
        self.parent = parent
        self.move = move
        self.g = 0
        self.h = self.calculate_heuristic()

    def __lt__(self, other):
        return (self.g + self.h) < (other.g + other.h)

    def calculate_heuristic(self):
        # manhattan distance heuristic
        distance = 0
        for i in range(3):
            for j in range(3):
                num = self.puzzle[i][j]
                if num != 0:
                    x = (num - 1) // 3
                    y = (num - 1) % 3
                    distance += abs(x - i) + abs(y - j)
        return distance

    def get_blank_position(self):
        # find the position of the blank tile (0)
        for i in range(3):
            for j in range(3):
                if self.puzzle[i][j] == 0:
                    return i, j

    def generate_possible_moves(self):
        # generate possible moves by swapping the blank tile with adjacent tiles
        moves = []
        i, j = self.get_blank_position()

        if i > 0:
            moves.append(("UP", i - 1, j))
        if i < 2:
            moves.append(("DOWN", i + 1, j))
        if j > 0:
            moves.append(("LEFT", i, j - 1))
        if j < 2:
            moves.append(("RIGHT", i, j + 1))

        return moves

    def generate_child_states(self):
        # generate child states by applying possible moves
        child_states = []
        moves = self.generate_possible_moves()

        for move, x, y in moves:
            i, j = self.get_blank_position()  # get the position of the blank tile
            new_puzzle = [row[:] for row in self.puzzle]  # create a copy of the puzzle
            new_puzzle[i][j], new_puzzle[x][y] = new_puzzle[x][y], new_puzzle[i][j]
            child_states.append(PuzzleState(new_puzzle, parent=self, move=move))

        return child_states

    def print_solution(self):
        moves = []
        states = []
        node = self
        while node:
            moves.append(node.move)
            states.append(node.puzzle)
            node = node.parent

        moves.reverse()
        states.reverse()

        print("Solution Path:")
        for move, state in zip(moves, states):
            if move:
                print("Move:", move)
            print_puzzle_state(state)
            print("")

def print_puzzle_state(state):
    print("-------------")
    for row in state:
        print("|", end=" ")
        for num in row:
            if num == 0:
                print(" ", end=" ")
            else:
                print(num, end=" ")
            print("|", end=" ")
        print("\n-------------")


def solve_puzzle(start_state):
    open_list = []
    closed_set = set()

    start_state.g = 0
    open_list.append(start_state)

    while open_list:
        current_state = heappop(open_list)
        closed_set.add(tuple(map(tuple, current_state.puzzle)))

        if current_state.puzzle == goal_state:
            current_state.print_solution()
            return

        child_states = current_state.generate_child_states()
        for child_state in child_states:
            if tuple(map(tuple, child_state.puzzle)) not in closed_set:
                child_state.g = current_state.g + 1
                heappush(open_list, child_state)

start_state = PuzzleState([[1, 2, 0], [3, 4, 6], [7, 5, 8]])
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]


solve_puzzle(start_state)

#time complexity of O(b^d), where b is the branching factor(number of possible moves) and d is the depth of the optimal solution.
#The A* algorithm continues exploring states until it finds the goal state or exhausts all possible states. 
# The time complexity of the A* algorithm depends on the number of states explored. In the worst case, 
# it explores all possible states, resulting in a time complexity of O(b^d), where b is the branching factor
# (number of possible moves) and d is the depth of the optimal solution.
#Space complexity of O(b^d),  dominated by the space required for the open list and closed set.The maximum size of the open list can be proportional to the number of states explored during the search. In the worst 
# case, where all states need to be explored, the space complexity of the open list is O(b^d) due to the branching factor and 
# depth of the optimal solution.The closed set stores unique puzzle configurations encountered during the search. The space complexity of the closed set is 
# also O(b^d) in the worst case.

# def get_user_input():
#     print("Enter the start state:")
#     start_state = []
#     for _ in range(3):
#         row = list(map(int, input().split()))
#         start_state.append(row)

#     print("Enter the goal state:")
#     goal_state = []
#     for _ in range(3):
#         row = list(map(int, input().split()))
#         goal_state.append(row)

#     return start_state, goal_state

# def solve_puzzle(start_state, goal_state):
#     # ...

# # Main program
# start_state, goal_state = get_user_input()
# start_state = PuzzleState(start_state)
# solve_puzzle(start_state, goal_state)
