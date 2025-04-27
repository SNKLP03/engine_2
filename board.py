# board.py

from move_generation import get_all_legal_moves_for_color

class Board:
    def __init__(self):
        # Correct constructor name: __init__
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
        self.move_log = []  # Store moves for undo

    def print_board(self):
        # Nicely print the board
        for row in self.board:
            print(' '.join(row))
        print()

    def move_piece(self, start_pos, end_pos):
        """Moves a piece from start_pos to end_pos and records the move."""
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        piece_moved = self.board[start_row][start_col]
        piece_captured = self.board[end_row][end_col]

        if piece_moved == " ":
            print("No piece at starting position!")
            return False

        # Move the piece
        self.board[end_row][end_col] = piece_moved
        self.board[start_row][start_col] = " "

        # Save the move (for undo later)
        self.move_log.append((start_pos, end_pos, piece_moved, piece_captured))

        # Switch the turn
        self.white_to_move = not self.white_to_move
        return True

    def undo_move(self):
        """Undo the last move."""
        if not self.move_log:
            return

        start_pos, end_pos, piece_moved, piece_captured = self.move_log.pop()
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        self.board[start_row][start_col] = piece_moved
        self.board[end_row][end_col] = piece_captured

        # Switch the turn back
        self.white_to_move = not self.white_to_move

    def find_king(self, white):
        """Find the position of the king for the given color."""
        king = 'K' if white else 'k'
        for row in range(8):
            for col in range(8):
                if self.board[row][col] == king:
                    return (row, col)
        return None  # Should never happen normally

    def is_in_check(self, white):
        """Check if the king of the given color is in check."""
        king_pos = self.find_king(white)
        if king_pos is None:
            return True  # King missing (error)

        # Get all opponent moves
        opponent_moves = get_all_legal_moves_for_color(self, not white)

        for move in opponent_moves:
            _, end_pos = move
            if end_pos == king_pos:
                return True
        return False

    def is_on_board(self, row, col):
        """Check if a position is inside the board."""
        return 0 <= row < 8 and 0 <= col < 8
