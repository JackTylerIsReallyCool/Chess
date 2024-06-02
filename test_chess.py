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

def test_square_to_indices():
    all_squares = [f"{col}{row}" for col in "abcdefgh" for row in "12345678"]
    
    for square in all_squares:
        row_index, col_index = square_to_indices(square)
        assert row_index < 8 and row_index >= 0
        assert col_index < 8 and col_index >= 0

def test_move_validtion():
    ranks = ['a','b','c','d','e','f','g','h','i']
    files = ['1','2','3','4','5','6','7','8','9']
    
    test_cases = [
        ["8/8/8/8/8/8/P7/8",2],
        ["8/8/8/8/8/P7/8/8",1],
        ["8/8/8/8/1p6/P7/8/8",2],
        ["8/8/8/8/1p6/8/P7/8",2],
        ["8/8/8/8/8/P7/P7/8",1],
        [STARTING_FEN, 20]
        ]
    
    current_fen = STARTING_FEN
    
    for test_case in test_cases:
        print("Testing", test_case[0])
        count_valid_moves = 0
        for start_rank in ranks:
            for start_file in files:
                for target_rank in ranks:
                    for target_file in files:
                        starting_square = start_rank + start_file
                        target_square = target_rank + target_file
                                            
                        if validate_move(test_case[0], starting_square, target_square, 'w'):
                            count_valid_moves += 1
        
        assert count_valid_moves == test_case[1]
        print("Passed")