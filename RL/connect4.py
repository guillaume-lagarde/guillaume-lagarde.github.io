class Game:
    def __init__(self):
        self.board = [["" for _ in range(7)] for _ in range(6)]
        self.current_player = 1  # Player 1 starts
        self.name = "Connect4"

    def get_valid_moves(self):
        moves = []
        for j in range(7):
            if self.board[0][j] == "":
                moves.append(j)
        return moves

    def make_move(self, column):
        for i in reversed(range(6)):
            if self.board[i][column] == "":
                self.board[i][column] = "X" if self.current_player == 1 else "O"
                self.current_player = 3 - self.current_player  # Switch player
                break

    def game_over(self):
        # Check rows, columns, diagonals for a win or if board is full
        # Return: (Boolean, Winner)

        # Check horizontal locations for win
        for r in range(6):
            for c in range(4):
                if (
                    self.board[r][c]
                    == self.board[r][c + 1]
                    == self.board[r][c + 2]
                    == self.board[r][c + 3]
                    != ""
                ):
                    return True, self.board[r][c]

        # Check vertical locations for win
        for c in range(7):
            for r in range(3):
                if (
                    self.board[r][c]
                    == self.board[r + 1][c]
                    == self.board[r + 2][c]
                    == self.board[r + 3][c]
                    != ""
                ):
                    return True, self.board[r][c]

        # Check positively sloped diagonals
        for c in range(4):
            for r in range(3):
                if (
                    self.board[r][c]
                    == self.board[r + 1][c + 1]
                    == self.board[r + 2][c + 2]
                    == self.board[r + 3][c + 3]
                    != ""
                ):
                    return True, self.board[r][c]

        # Check negatively sloped diagonals
        for c in range(4):
            for r in range(3, 6):
                if (
                    self.board[r][c]
                    == self.board[r - 1][c + 1]
                    == self.board[r - 2][c + 2]
                    == self.board[r - 3][c + 3]
                    != ""
                ):
                    return True, self.board[r][c]

        if self.get_valid_moves() == []:
            return True, None

        return False, None
    
    def is_game_over(self):
        return self.game_over()[0]

    def print_board(self):
        for row in self.board:
            print("|", end="")
            for cell in row:
                symbol = cell if cell else " "
                print(f" {symbol} |", end="")
            print("\n" + "-" * 29)
