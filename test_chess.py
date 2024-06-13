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
    actual_board = decode_fen(starting_fen)
    
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

def test_square_to_indices():
    all_squares = [f"{col}{row}" for col in "abcdefgh" for row in "12345678"]
    
    for square in all_squares:
        row_index, col_index = square_to_indices(square)
        assert row_index < 8 and row_index >= 0
        assert col_index < 8 and col_index >= 0

def test_move_validation():
    white_pawn_test_cases = [
        {
            "fen": "8/8/8/8/8/8/P7/8",
            "expected_moves": [("a2", "a3"), ("a2", "a4")],
            "current_color": 'w'
        },
        {
            "fen": "8/8/8/8/8/P7/8/8",
            "expected_moves": [("a3", "a4")],
            "current_color": 'w'
        },
        {
            "fen": "8/8/8/8/1p6/P7/8/8",
            "expected_moves": [("a3", "a4"), ("a3", "b4")],
            "current_color": 'w'
        },
        {
            "fen": "8/8/8/8/8/P7/P7/8",
            "expected_moves": [("a3", "a4")],
            "current_color": 'w'
        },
        {
            "fen": "8/8/8/8/P7/8/P7/8",
            "expected_moves": [("a2", "a3"), ("a4", "a5")],
            "current_color": 'w'
        },
        {
            "fen": "8/8/8/8/8/1p6/P7/8",
            "expected_moves": [("a2", "b3"), ("a2", "a3"), ("a2", "a4")],
            "current_color": 'w'
        },
        {
            "fen": "8/8/8/8/8/p1p5/1P6/8",
            "expected_moves": [("b2", "a3"), ("b2", "c3"), ("b2", "b3"), ("b2", "b4")],
            "current_color": 'w'
        },
        {
            "fen": "8/8/8/8/8/1p6/1P6/8",
            "expected_moves": [],
            "current_color": 'w'
        },
    ]

    black_pawn_test_cases = [
        {
            "fen": "8/p7/8/8/8/8/8/8",
            "expected_moves": [("a7", "a6"), ("a7", "a5")],
            "current_color": 'b'
        },
        {
            "fen": "8/8/p7/8/8/8/8/8",
            "expected_moves": [("a6", "a5")],
            "current_color": 'b'
        },
        {
            "fen": "8/8/p7/1P6/8/8/8/8",
            "expected_moves": [("a6", "a5"), ("a6", "b5")],
            "current_color": 'b'
        },
        {
            "fen": "8/p7/1P6/1P6/8/8/8/8",
            "expected_moves": [("a7", "a6"), ("a7", "a5"), ("a7", "b6")],
            "current_color": 'b'
        },
        {
            "fen": "8/p7/p7/8/8/8/8/8",
            "expected_moves": [("a6", "a5")],
            "current_color": 'b'
        },
        {
            "fen": "8/p7/8/p7/8/8/8/8",
            "expected_moves": [("a7", "a6"), ("a5", "a4")],
            "current_color": 'b'
        },
        {
            "fen": "8/1p6/1P6/8/8/8/8/8",
            "expected_moves": [],
            "current_color": 'b'
        }
    ]
    
    test_cases = white_pawn_test_cases + black_pawn_test_cases

    ranks = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    files = ['1', '2', '3', '4', '5', '6', '7', '8']

    for test_case in test_cases:
        fen = test_case["fen"]
        expected_moves = test_case["expected_moves"]
        current_color = test_case["current_color"]
        print("Testing", fen)
        actual_moves = []
        for start_rank in ranks:
            for start_file in files:
                for target_rank in ranks:
                    for target_file in files:
                        starting_square     = start_rank + start_file
                        target_square = target_rank + target_file
                                            
                        if validate_move(fen, starting_square, target_square, current_color):
                            actual_moves.append((starting_square, target_square))
        
        assert set(actual_moves) == set(expected_moves), f"Expected {expected_moves}, but got {actual_moves}"
        print("Passed")