import os
import re
from time import time

""" 
A number maze M[1..n, 1..n] is an n by n grid of non-negative integers.
A token is initially placed in the upper left corner, on the square (1,1).
We want to move it to the lower right corner, the square (n,n), using a minimum number of moves. 
If the token is on square (i,j), then in a single move, we can move it up, down, left, or right, by M[i,j] squares. 
(Of course, any such move is valid only if we stay within the grid.) 
Note that in this assignment we allow M[i,j] to be 0; if the token reaches such a square (i,j), it cannot move any further.
"""


def printMaze(M, n, token):
    for i in range(n):
        for j in range(n):
            if (i, j) == token:
                print("#", end=" ")
            else:
                if M[i][j] == 0:
                    print("  ", end="")
                else:
                    print(M[i][j], end=" ")
        print()


def mazeSolver(grid, n):
    start, end = (0, 0), (n-1, n-1)
    moves = ((0, 1), (1, 0), (0, -1), (-1, 0))
    queue, costs = [start], {start: 0}
    
    visited = set()
    while queue:
        (x, y) = queue.pop(0)
        if (x, y) == end: # Goal reached
            return costs[(x, y)]

        if grid[x][y] != 0:
            if (x, y) not in visited:
                visited.add((x, y))
                for dx, dy in moves:
                    new_x = x + dx * grid[x][y]
                    new_y = y + dy * grid[x][y]
                    if 0 <= new_x < n and 0 <= new_y < n:
                        if grid[new_x][new_y] != 0:
                            if (new_x, new_y) not in costs or costs[(new_x, new_y)] > costs[(x, y)] + 1:
                                costs[(new_x, new_y)] = costs[(x, y)] + 1
                                queue.append((new_x, new_y))
    return -1


def main():

    path = os.getcwd()+"\\tests\\"
    testdir = os.listdir(path)
    #test = path+input('Input: ')+".txt"
    temp_test = "C:\\Users\\Miles\\Desktop\\hw6\\tests\\smallE.txt"

    with open(temp_test) as data:
        A = [eval(s.strip()) for s in data.readlines()]
        n = A[0]
        A = A[1:]
        M = [A[i:i+n] for i in range(0, len(A), n)]
        move_cost = mazeSolver(M, n)
        if move_cost > 0:
            print("Output: ", move_cost)
        else:
            print("Output: No solution")


if __name__ == '__main__':
    main()
