# Documentation

(a)
    My algorithm's structure is based on Dijkstra's shortest path algorithm. A queue stores the token positions to be checked. A visited set is used to store the positions that have already been checked.At any position, I check the 4 adjacent positions and add them to the queue if they are valid. A distance map then keeps track of the minimum number of moves taken to reach the current position. The algorithm terminates when the queue is empty or the destination is reached.

(b)

    n = 1000
        LargeE.txt
        Shortest path cost:  55
        Runtime: 51227.74243354797ms

        LargeF.txt
        Shortest path cost:  56
        Runtime: 53568.77660751343ms
    n = 100
        MediumE.txt
        Shortest path cost:  65
        Runtime: 23.996829986572266ms

        MediumF.txt
        Shortest path cost:  64
        Runtime: 16.066551208496094ms
    n = 10
        SmallE.txt
        Shortest path cost:  8
        Runtime: 0.0ms

        SmallF.txt
        Shortest path cost:  7
        Runtime: 0.0ms

(c) Requires Python 3.10.4 or higher
    Run the program with
        py hw6.py
