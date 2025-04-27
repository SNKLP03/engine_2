# move_generation_helper.py

def is_opponent_piece(piece, target_piece):
    if piece.isupper() and target_piece.islower():
        return True
    if piece.islower() and target_piece.isupper():
        return True
    return False


def generate_piece_moves(board_obj, piece, row, col):
    moves = []

    if piece.lower() == "p":
        # Pawn moves
        direction = -1 if piece.isupper() else 1
        start_row = 6 if piece.isupper() else 1

        # Move forward
        if board_obj.is_on_board(row + direction, col) and board_obj.board[row + direction][col] == " ":
            moves.append(((row, col), (row + direction, col)))

            # First double move
            if row == start_row and board_obj.is_on_board(row + 2 * direction, col) and board_obj.board[row + 2 * direction][col] == " ":
                moves.append(((row, col), (row + 2 * direction, col)))

        # Captures
        for dc in [-1, 1]:
            if board_obj.is_on_board(row + direction, col + dc):
                target_piece = board_obj.board[row + direction][col + dc]
                if target_piece != " " and is_opponent_piece(piece, target_piece):
                    moves.append(((row, col), (row + direction, col + dc)))

    elif piece.lower() == "n":
        # Knight moves
        knight_moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                        (1, -2), (1, 2), (2, -1), (2, 1)]

        for dr, dc in knight_moves:
            new_row = row + dr
            new_col = col + dc
            if board_obj.is_on_board(new_row, new_col):
                dest_piece = board_obj.board[new_row][new_col]
                if dest_piece == " " or is_opponent_piece(piece, dest_piece):
                    moves.append(((row, col), (new_row, new_col)))

    elif piece.lower() == "k":
        # King moves
        king_moves = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1), (1, 0), (1, 1)]

        for dr, dc in king_moves:
            new_row = row + dr
            new_col = col + dc
            if board_obj.is_on_board(new_row, new_col):
                dest_piece = board_obj.board[new_row][new_col]
                if dest_piece == " " or is_opponent_piece(piece, dest_piece):
                    moves.append(((row, col), (new_row, new_col)))

    else:
        # Sliding pieces: rook, bishop, queen
        directions = []

        if piece.lower() == "r":
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Straight lines
        elif piece.lower() == "b":
            directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # Diagonals
        elif piece.lower() == "q":
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                          (-1, -1), (-1, 1), (1, -1), (1, 1)]  # Queen = all

        for dr, dc in directions:
            for i in range(1, 8):
                new_row = row + dr * i
                new_col = col + dc * i
                if board_obj.is_on_board(new_row, new_col):
                    dest_piece = board_obj.board[new_row][new_col]
                    if dest_piece == " ":
                        moves.append(((row, col), (new_row, new_col)))
                    elif is_opponent_piece(piece, dest_piece):
                        moves.append(((row, col), (new_row, new_col)))
                        break
                    else:
                        break
                else:
                    break

    return moves
