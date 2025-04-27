# search.py

from move_generation import get_all_legal_moves
from evaluate import evaluate_board

def minimax(board_obj, depth, alpha, beta, maximizing_player):
    """Minimax search with alpha-beta pruning."""
    if depth == 0:
        return evaluate_board(board_obj), None

    possible_moves = get_all_legal_moves(board_obj)

    if not possible_moves:
        # No legal moves (checkmate or stalemate)
        return evaluate_board(board_obj), None

    best_move = None

    if maximizing_player:
        max_eval = -float('inf')
        for move in possible_moves:
            start, end = move

            # Make the move
            board_obj.move_piece(start, end)

            evaluation, _ = minimax(board_obj, depth - 1, alpha, beta, False)

            # Undo the move
            board_obj.undo_move()

            if evaluation > max_eval:
                max_eval = evaluation
                best_move = move

            alpha = max(alpha, evaluation)
            if beta <= alpha:
                break  # Beta cutoff

        return max_eval, best_move

    else:
        min_eval = float('inf')
        for move in possible_moves:
            start, end = move

            # Make the move
            board_obj.move_piece(start, end)

            evaluation, _ = minimax(board_obj, depth - 1, alpha, beta, True)

            # Undo the move
            board_obj.undo_move()

            if evaluation < min_eval:
                min_eval = evaluation
                best_move = move

            beta = min(beta, evaluation)
            if beta <= alpha:
                break  # Alpha cutoff

        return min_eval, best_move
