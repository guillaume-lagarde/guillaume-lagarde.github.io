class Game:
    def __init__(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = 1  # Player 1 starts
        self.name = "TicTacToe"

    def get_valid_moves(self):
        moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    moves.append((i, j))
        return moves

    def make_move(self, move):
        if self.board[move[0]][move[1]] == "":
            self.board[move[0]][move[1]] = "X" if self.current_player == 1 else "O"
            self.current_player = 3 - self.current_player  # Switch player

    def game_over(self):
        # Check rows, columns, diagonals for a win or if board is full
        # Return: (Boolean, Winner)
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True, self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True, self.board[0][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True, self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True, self.board[0][2]
        if self.get_valid_moves() == []:
            return True, None
        return False, None
    
    def is_game_over(self):
        return self.game_over()[0]

    def print_board(self):
        horizontal_line = "+---+---+---+"
        print("Game state:")
        for i in range(3):
            print(horizontal_line)
            for j in range(3):
                print(
                    f"| {self.board[i][j] if self.board[i][j] != '' else ' '} ", end=""
                )
            print("|")
        print(horizontal_line)


# test the game
game = Game()
game.print_board()
print(game.get_valid_moves())
game.make_move((0, 0))
game.print_board()
print(game.get_valid_moves())
game.make_move((1, 1))
game.print_board()
print(game.get_valid_moves())
game.make_move((0, 1))
game.print_board()
print(game.get_valid_moves())
game.make_move((1, 0))
game.print_board()
print(game.get_valid_moves())
game.make_move((0, 2))
game.print_board()
print(game.get_valid_moves())
print(game.game_over())
