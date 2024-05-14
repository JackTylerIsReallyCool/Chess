from chess import *

STARTING_BOARD = [
        ["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"],
        ["♟", "♟", "♟", "♟", "♟", "♟", "♟", "♟"],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        ["♙", "♙", "♙", "♙", "♙", "♙", "♙", "♙"],
        ["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"]
    ]

def test_board_from_fen():
    starting_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
    
    expected_board = STARTING_BOARD
    actual_board = board_from_fen(starting_fen)
    
    assert actual_board == expected_board
    
def test_format_board():
    board = STARTING_BOARD
    formatted_board = format_board(board)
    
    expected_output = (
        "  a b c d e f g h\n"
        " +-----------------+\n"
        "8| ♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜ |\n"
        "7| ♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟ |\n"
        "6|                 |\n"
        "5|                 |\n"
        "4|                 |\n"
        "3|                 |\n"
        "2| ♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙ |\n"
        "1| ♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖ |\n"
        " +-----------------+\n"
        "  a b c d e f g h"
    )
    
    assert formatted_board == expected_output