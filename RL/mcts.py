from math import sqrt, log
import random
from copy import deepcopy

# from ticTacToe import Game
from connect4 import Game

HUMAN = False

class Node:
    def __init__(self, game_state, parent=None, move=None):
        self.game_state = game_state
        self.parent = parent  # "None" for the root node
        self.move = move  # The move that led to this node from the parent node
        self.children = []  # List of child nodes
        self.visits = 0  # Number of times this node was visited
        self.wins = 0  # Number of wins from this node
        self.untried_moves = game_state.get_valid_moves()

    def has_untried_moves(self):
        return len(self.untried_moves) > 0

    def has_children(self):
        return len(self.children) > 0

    def select_child(self):
        """
        Use the UCT (Upper Confidence bound applied to Trees) formula to select the best child node.
        UCT formula: c = child.wins/child.visits + sqrt(2 * log(self.visits)/child.visits)
        (Other possibility: use an espilon-greedy policy to select the best child node.)

        The node should be selected according to the player who is playing in the current state. Player 1 wants to maximize the value, while player 2 wants to minimize it.
        """
        # TO FILL
        return random.choice(self.children)
    
    def expand(self):
        """
        Expand the current node by creating a new child node (taken from the list of untried moves)
        """
        move = random.choice(self.untried_moves)
        self.untried_moves.remove(move)
        new_game_state = deepcopy(
            self.game_state
        )  # Create a deep copy to avoid mutating the original game state
        new_game_state.make_move(move)
        child_node = Node(game_state=new_game_state, parent=self, move=move)
        self.children.append(child_node)
        return child_node

    def update(self, result):
        """
        Update node information after a simulation.
        """
        # TO FILL
        pass


def run_mcts(root, iterations=3000):
    """ 
    Run Monte Carlo Tree Search for a number of iterations starting from a given (root) node.
    Return the best move from the root node.
    """

    current_player = root.game_state.current_player

    for _ in range(iterations):
        node = root
        game = deepcopy(node.game_state)  # Copy current game state

        # 1. Selection
        while not node.has_untried_moves() and node.has_children():
            # TO FILL
            pass

        # 2. Expansion
        if node.has_untried_moves() and not game.is_game_over():
            # TO FILL
            pass
        
        # 3. Simulation: rollout to the end of the game using a random strategy
        while not game.is_game_over():
            # TO FILL
            pass

        # 4. Backpropagation
        #  the winner is 1 if it is "X", 2 if it is "O" and 0 if it is a draw
        winner = 1 if game.game_over()[1] == "X" else 2
        if game.game_over()[1] == None:
            winner = 0

        while node != root.parent:
            result = 0
            if winner == current_player:
                result = 1
            elif winner == 3 - current_player:
                result = -1
            else:
                result = 0
            node.update(result)
            node = node.parent

    # After all iterations, return the move of the child with the highest winrate
    return max(root.children, key=lambda child: child.wins / child.visits).move




def run_game(Node, number_of_iterations, human=False, verbose=False):
    game = Game()
    root = Node(game_state=game)
    print("X starts the game and O plays second")
    print("X is the IA")
    while not game.game_over()[0]:
        if game.current_player == 1:
            best_move = run_mcts(root, number_of_iterations)
            game.make_move(best_move)
        else:
            if not human:
                best_move = random.choice(game.get_valid_moves())
                game.make_move(best_move)
            else:
                print("valid moves:", game.get_valid_moves())
                chosen_move = input("Enter a valid move: ")
                if game.name == "TicTacToe":
                    chosen_move = tuple(int(x.strip()) for x in chosen_move.split(","))
                elif game.name == "Connect4":
                    chosen_move = int(chosen_move)
                else:
                    raise ValueError("game name not recognized")
                game.make_move(chosen_move)

        # Update the root to the child node that corresponds to the chosen move
        for child in root.children:
            if child.move == best_move:
                parent = root
                root = child
                root.parent = parent
                break

        if verbose:
            game.print_board()
    if verbose:
        print("Winner:", game.game_over()[1])

    return game.game_over()[1]


# run N games and compute the winrate of the IA
N = 10
wins = 0
loose = 0
draw = 0
number_of_iterations_mcts = 500

for i in range(N):
    print(f"Game {i+1}/{N}")
    winner = run_game(Node, number_of_iterations_mcts, verbose=True, human=HUMAN)
    if winner == "X":
        wins += 1
    elif winner == "O":
        loose += 1
    else:
        draw += 1

print("number of wins: {}/{}".format(wins, N))
print("number of loose: {}/{}".format(loose, N))
print("number of draw: {}/{}".format(draw, N))
