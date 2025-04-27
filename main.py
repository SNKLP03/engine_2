# main.py

from board import Board
from move_generation import get_all_legal_moves
from search import minimax

def main():
    game_board = Board()
    game_board.print_board()

    debug_mode = True

    while True:
        try:
            legal_moves = get_all_legal_moves(game_board)
        except Exception as e:
            print(f"Error generating legal moves: {e}")
            game_board.print_board()
            break

        if not legal_moves:
            if game_board.is_in_check(game_board.white_to_move):
                print("Checkmate!")
                print(f"{'White' if game_board.white_to_move else 'Black'} is in check with no legal moves.")
            else:
                print("Stalemate!")
                print("No legal moves, but not in check.")
            break

        player = "White" if game_board.white_to_move else "Black"
        print(f"{player}'s move:")

        if debug_mode:
            print("Legal moves:", legal_moves)

        if game_board.white_to_move:
            # Human move
            while True:
                try:
                    start = input("Enter start position (row col): ").split()
                    end = input("Enter end position (row col): ").split()

                    if len(start) != 2 or len(end) != 2:
                        print("Invalid input. Please enter two numbers separated by a space.")
                        continue

                    start_pos = (int(start[0]), int(start[1]))
                    end_pos = (int(end[0]), int(end[1]))

                    move = (start_pos, end_pos)
                    if move not in legal_moves:
                        print(f"Illegal move: {move} not in legal moves. Try again.")
                        continue

                    if not game_board.move_piece(start_pos, end_pos):
                        print("Move rejected by board. Try again.")
                        game_board.print_board()
                        continue

                    break  # Move successful

                except ValueError:
                    print("Invalid input. Please enter valid numbers.")
                    continue
        else:
            # Engine move
            print("Engine thinking...")
            print("Board before minimax:")
            game_board.print_board()

            _, best_move = minimax(game_board, depth=4, alpha=-float('inf'), beta=float('inf'), maximizing_player=False)

            if best_move is None:
                print("No moves left. Game over!")
                break

            print(f"Engine moves from {best_move[0]} to {best_move[1]}")
            print("Board before engine move:")
            game_board.print_board()

            if not game_board.move_piece(best_move[0], best_move[1]):
                print(f"Engine move {best_move} rejected. Terminating game.")
                game_board.print_board()
                break

        game_board.print_board()

if __name__ == "__main__":
    main()
