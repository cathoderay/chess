Chess
=====

It is still a WIP, just for fun. Soon -- I hope, going to be a chess engine/player. 

## Current step
Currently modelling the chess rules.

## Performance
Don't care for a while...

## Test coverage

    Sat Oct 6 03:00:28 BRT 2012
    ============================= test session starts ==============================
    platform linux2 -- Python 2.7.2 -- pytest-2.2.4
    collecting ... collected 61 items
    
    tests/test_board.py ..................
    tests/test_pawn.py ............
    tests/test_piece.py .....
    tests/test_square.py ..........................
    --------------- coverage: platform linux2, python 2.7.2-final-0 ----------------
    Name                Stmts   Miss  Cover   Missing
    -------------------------------------------------
    board                  61     12    80%   45, 61-62, 74, 79-89
    conf                    4      0   100%   
    exception               2      0   100%   
    pawn                   38      0   100%   
    piece                  14      2    86%   16, 19
    square                 64      0   100%   
    tests/test_board      103      0   100%   
    tests/test_pawn        85      0   100%   
    tests/test_piece       32      0   100%   
    tests/test_square     108      0   100%   
    -------------------------------------------------
    TOTAL                 511     14    97%   
    
    ========================== 61 passed in 0.56 seconds ===========================

## Help
Feel free, ;)
