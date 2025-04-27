# move_generation.py

from move_generation_helper import generate_piece_moves

def get_all_legal_moves(board_obj):
    """Generate all legal moves for the player whose turn it is."""
    moves = []

    for row in range(8):
        for col in range(8):
            piece = board_obj.board[row][col]
            if piece == " ":
                continue

            if (board_obj.white_to_move and piece.isupper()) or (not board_obj.white_to_move and piece.islower()):
                piece_moves = generate_piece_moves(board_obj, piece, row, col)

                for move in piece_moves:
                    start, end = move

                    # Make the move temporarily
                    captured_piece = board_obj.board[end[0]][end[1]]
                    board_obj.board[end[0]][end[1]] = piece
                    board_obj.board[start[0]][start[1]] = " "

                    # Switch turn
                    board_obj.white_to_move = not board_obj.white_to_move

                    if not board_obj.is_in_check(not board_obj.white_to_move):
                        moves.append(move)

                    # Undo move
                    board_obj.board[start[0]][start[1]] = piece
                    board_obj.board[end[0]][end[1]] = captured_piece
                    board_obj.white_to_move = not board_obj.white_to_move

    return moves

def get_all_legal_moves_for_color(board_obj, white):
    """Get all pseudo-legal moves for a specific color (no king safety checks)."""
    moves = []

    for row in range(8):
        for col in range(8):
            piece = board_obj.board[row][col]
            if piece == " ":
                continue

            if (white and piece.isupper()) or (not white and piece.islower()):
                moves.extend(generate_piece_moves(board_obj, piece, row, col))

    return moves
