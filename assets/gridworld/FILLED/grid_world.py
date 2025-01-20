import random

class GridWorldMDP:
    def __init__(self, height: int, width: int, number_of_holes: int):
        self.height = height
        self.width = width
        self.number_of_holes = number_of_holes

        self.states = set((i, j) for i in range(height) for j in range(width))

        UP = (-1, 0)
        DOWN = (1, 0)
        LEFT = (0, -1)
        RIGHT = (0, 1)

        self.actions = [UP, DOWN, LEFT, RIGHT]

        self.bad_states = random.sample(list(self.states - {(0, 0), (height - 1, width - 1)}), self.number_of_holes)

        self.initial_state = (0, 0)
        self.terminal_state = (height - 1, width - 1)

        self.transition_probabilities = {(state, action, new_state): 0 for state in self.states for action in self.actions for new_state in self.states} # a dictionary of type "{(s,a,s') : probability of the transition(s,a,s')}"
        self.rewards = {(state, action, new_state): 0 for state in self.states for action in self.actions for new_state in self.states} # a dictionary of type "{(s,a,s') : reward of the transition(s,a,s')}"

        for state in self.states:
            if state in self.bad_states or state == self.terminal_state:
                continue
            for action in self.actions:
                new_state = (state[0] + action[0], state[1] + action[1])
                if new_state not in self.states:
                    new_state = state
                self.transition_probabilities[(state, action, new_state)] = 1
                if new_state == self.terminal_state:
                    self.rewards[(state, action, new_state)] = 1
                else:
                    self.rewards[(state, action, new_state)] = 0

    def print_board(self):
        cell_width = 3
        horizontal_border = "+" + ("-" * cell_width + "+") * self.width

        print(horizontal_border)
        for i in range(self.height):
            row = "|"
            for j in range(self.width):
                if (i, j) == self.terminal_state:
                    cell = "T".center(cell_width)
                elif (i, j) in self.bad_states:
                    cell = "X".center(cell_width)
                else:
                    cell = ".".center(cell_width)
                row += cell + "|"
            print(row)
            print(horizontal_border)
        print()


    def print_policy(self, policy: dict):
        cell_width = 3

        horizontal_border = "+" + ("-" * cell_width + "+") * self.width

        print(horizontal_border)
        for i in range(self.height):
            row = "|"
            for j in range(self.width):
                if (i, j) == self.terminal_state:
                    cell = "T".center(cell_width)
                elif (i, j) in self.bad_states:
                    cell = "X".center(cell_width)
                else:
                    action = policy[(i, j)]
                    # Use arrows to represent actions
                    if action == (1, 0):
                        cell = "↓".center(cell_width)
                    elif action == (-1, 0):
                        cell = "↑".center(cell_width)
                    elif action == (0, 1):
                        cell = "→".center(cell_width)
                    elif action == (0, -1):
                        cell = "←".center(cell_width)
                    else:
                        cell = " ".center(cell_width)  # Fallback for undefined actions
                row += cell + "|"
            print(row)
            print(horizontal_border)
        print()


    def print_value_function(self, V):
        max_length = max(len(f"{V.get((i, j), 0):.2f}") for i in range(self.height) for j in range(self.width))

        cell_width = max_length + 2
        horizontal_border = "+" + ("-" * cell_width + "+") * self.width

        print(horizontal_border)
        for i in range(self.height):
            row = "|"
            for j in range(self.width):
                if (i, j) == self.terminal_state:
                    cell = "T".center(cell_width)
                elif (i, j) in self.bad_states:
                    cell = "X".center(cell_width)
                else:
                    cell = f"{V.get((i, j), 0):.2f}".center(cell_width)
                row += cell + "|"
            print(row)
            print(horizontal_border)
        print()

### Test
grid = GridWorldMDP(10, 4, 4)
grid.print_board()
random_policy = {state: random.choice(grid.actions) for state in grid.states}
print(random_policy[(0, 0)])
grid.print_policy(random_policy)

random_value = {state: random.random() for state in grid.states}
grid.print_value_function(random_value)