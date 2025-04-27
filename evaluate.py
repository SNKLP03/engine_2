# evaluate.py

# Piece values for evaluation
piece_values = {
    "p": 100,
    "n": 320,
    "b": 330,
    "r": 500,
    "q": 900,
    "k": 20000  # King value (very high to prevent losing)
}

def evaluate_board(board_obj):
    """Evaluate the board position based on material balance."""
    score = 0

    for row in board_obj.board:
        for piece in row:
            if piece == " ":
                continue
            if piece.isupper():
                score += piece_values.get(piece.lower(), 0)
            else:
                score -= piece_values.get(piece.lower(), 0)

    return score
