(a) 
    My algorithm's structure is based on the textbooks WhateverFirstSearch. A queue stores the positions to be checked. At any position, I check the 4 adjacent positions and add them to the queue if they are valid. A map to keeps track of the minimum number of moves taken to reach the current position. A visited set is used to store the positions that have already been checked.

(b)
    n = 10
        SmallF
        Minimum number of moves:
        Running time:

        SmallE
        Minimum number of moves:
        Running time:

    n = 100
        MediumF
        Minimum number of moves:
        Running time:

        MediumE
        Minimum number of moves:
        Running time:

    n = 1000
        LargeF
        Minimum number of moves:
        Running time:

        LargeE
        Minimum number of moves:
        Running time:

(c) Requires Python 3.10.4
    Run the program with
        py hw6.py
