# move_generation.py

from move_generation_helper import generate_piece_moves, is_opponent_piece

def get_all_legal_moves(board_obj):
    moves = []
    for row in range(8):
        for col in range(8):
            piece = board_obj.board[row][col]
            if piece == " ":
                continue
            if (piece.isupper() and board_obj.white_to_move) or (piece.islower() and not board_obj.white_to_move):
                piece_moves = generate_piece_moves(board_obj, piece, row, col)
                for move in piece_moves:
                    start_pos, end_pos = move

                    # Make the move temporarily
                    captured_piece = board_obj.board[end_pos[0]][end_pos[1]]
                    board_obj.board[end_pos[0]][end_pos[1]] = piece
                    board_obj.board[start_pos[0]][start_pos[1]] = " "

                    in_check = board_obj.is_in_check(board_obj.white_to_move)

                    # Undo the move
                    board_obj.board[start_pos[0]][start_pos[1]] = piece
                    board_obj.board[end_pos[0]][end_pos[1]] = captured_piece

                    if not in_check:
                        moves.append(move)
    return moves


def get_all_legal_moves_for_color(board_obj, white):
    moves = []
    for row in range(8):
        for col in range(8):
            piece = board_obj.board[row][col]
            if piece == " ":
                continue
            if (piece.isupper() and white) or (piece.islower() and not white):
                piece_moves = generate_piece_moves(board_obj, piece, row, col)
                moves.extend(piece_moves)
    return moves
