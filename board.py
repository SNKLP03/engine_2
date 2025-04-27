# board.py
from move_generation import get_all_legal_moves_for_color

class Board:
    def __init__(self):
        self.board = [
            ["r", "n", "b", "q", "k", "b", "n", "r"],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            ["R", "N", "B", "Q", "K", "B", "N", "R"]
        ]
        self.white_to_move = True
        self.move_log = []  # store move history for undo

    def print_board(self):
        for row in self.board:
            print(' '.join(row))
        print()

    def move_piece(self, start_pos, end_pos):
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        piece_moved = self.board[start_row][start_col]
        piece_captured = self.board[end_row][end_col]

        if piece_moved == " ":
            print("No piece at starting position!")
            return False

        # Make the move
        self.board[end_row][end_col] = piece_moved
        self.board[start_row][start_col] = " "

        # Save the move in move_log
        self.move_log.append((start_pos, end_pos, piece_moved, piece_captured))

        # Switch turn
        self.white_to_move = not self.white_to_move

        return True

    def undo_move(self):
        if not self.move_log:
            return

        last_move = self.move_log.pop()
        start_pos, end_pos, piece_moved, piece_captured = last_move

        start_row, start_col = start_pos
        end_row, end_col = end_pos

        self.board[start_row][start_col] = piece_moved
        self.board[end_row][end_col] = piece_captured

        self.white_to_move = not self.white_to_move

    def is_in_check(self, white):
        king_pos = self.find_king(white)
        if king_pos is None:
            return True
        
        opponent_moves = get_all_legal_moves_for_color(self, not white)

        for move in opponent_moves:
            _, end_pos = move
            if end_pos == king_pos:
                return True
        return False
