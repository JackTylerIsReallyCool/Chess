WHITE_PAWN_TEST_CASES = [
    {
        "fen": "8/8/8/8/8/8/P7/8",
        "expected_moves": [("a2", "a3"), ("a2", "a4")],
        "current_color": "w",
    },
    {"fen": "8/8/8/8/8/P7/8/8", "expected_moves": [("a3", "a4")], "current_color": "w"},
    {
        "fen": "8/8/8/8/1p6/P7/8/8",
        "expected_moves": [("a3", "a4"), ("a3", "b4")],
        "current_color": "w",
    },
    {
        "fen": "8/8/8/8/8/P7/P7/8",
        "expected_moves": [("a3", "a4")],
        "current_color": "w",
    },
    {
        "fen": "8/8/8/8/P7/8/P7/8",
        "expected_moves": [("a2", "a3"), ("a4", "a5")],
        "current_color": "w",
    },
    {
        "fen": "8/8/8/8/8/1p6/P7/8",
        "expected_moves": [("a2", "b3"), ("a2", "a3"), ("a2", "a4")],
        "current_color": "w",
    },
    {
        "fen": "8/8/8/8/8/p1p5/1P6/8",
        "expected_moves": [("b2", "a3"), ("b2", "c3"), ("b2", "b3"), ("b2", "b4")],
        "current_color": "w",
    },
    {"fen": "8/8/8/8/8/1p6/1P6/8", "expected_moves": [], "current_color": "w"},
]

BLACK_PAWN_TEST_CASES = [
    {
        "fen": "8/p7/8/8/8/8/8/8",
        "expected_moves": [("a7", "a6"), ("a7", "a5")],
        "current_color": "b",
    },
    {"fen": "8/8/p7/8/8/8/8/8", "expected_moves": [("a6", "a5")], "current_color": "b"},
    {
        "fen": "8/8/p7/1P6/8/8/8/8",
        "expected_moves": [("a6", "a5"), ("a6", "b5")],
        "current_color": "b",
    },
    {
        "fen": "8/p7/1P6/1P6/8/8/8/8",
        "expected_moves": [("a7", "a6"), ("a7", "a5"), ("a7", "b6")],
        "current_color": "b",
    },
    {
        "fen": "8/p7/p7/8/8/8/8/8",
        "expected_moves": [("a6", "a5")],
        "current_color": "b",
    },
    {
        "fen": "8/p7/8/p7/8/8/8/8",
        "expected_moves": [("a7", "a6"), ("a5", "a4")],
        "current_color": "b",
    },
    {"fen": "8/1p6/1P6/8/8/8/8/8", "expected_moves": [], "current_color": "b"},
]

test_cases = WHITE_PAWN_TEST_CASES + BLACK_PAWN_TEST_CASES
