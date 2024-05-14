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
    'r': WHITE_ROOK,
    'n': WHITE_KNIGHT,
    'b': WHITE_BISHOP,
    'q': WHITE_QUEEN,
    'k': WHITE_KING,
    'p': WHITE_PAWN,
    'R': BLACK_ROOK,
    'N': BLACK_KNIGHT,
    'B': BLACK_BISHOP,
    'Q': BLACK_QUEEN,
    'K': BLACK_KING,
    'P': BLACK_PAWN,
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
    
    
def format_board(board):
    column_labels = '  a b c d e f g h'
    formatted_board = [column_labels]
    formatted_board.append(' +-----------------+')
    
    for i, row in enumerate(board):
        formatted_board.append(f"{8 - i}| {' '.join(row)} |")
    
    formatted_board.append(' +-----------------+')
    formatted_board.append(column_labels)
    
    return "\n".join(formatted_board)
