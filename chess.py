BLACK_ROOK = "♜"
BLACK_KNIGHT = "♞"
BLACK_BISHOP = "♝"
BLACK_QUEEN = "♛"
BLACK_KING = "♚"
BLACK_PAWN = "♟"
WHITE_ROOK = "♖"
WHITE_KNIGHT = "♘"
WHITE_BISHOP = "♗"
WHITE_QUEEN = "♕"
WHITE_KING = "♔"
WHITE_PAWN = "♙"
EMPTY = " "

PIECE_SYMBOLS = {
    'r': BLACK_ROOK,
    'n': BLACK_KNIGHT,
    'b': BLACK_BISHOP,
    'q': BLACK_QUEEN,
    'k': BLACK_KING,
    'p': BLACK_PAWN,
    'R': WHITE_ROOK,
    'N': WHITE_KNIGHT,
    'B': WHITE_BISHOP,
    'Q': WHITE_QUEEN,
    'K': WHITE_KING,
    'P': WHITE_PAWN,
}

STARTING_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"

def board_from_fen(fen):
    board = []
    
    rows = fen.split('/')
    
    for row in rows:
        
        board_row = []
        
        for char in row:
            if char.isdigit():
                board_row.extend([EMPTY] * int(char))
            else:
                board_row.append(PIECE_SYMBOLS[char])
                
        board.append(board_row)
                
    return board
    