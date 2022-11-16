import os
import re
from time import time


def printMaze(M, n):
    for i in range(n):
        for j in range(n):
            if (i, j) == (0, 0):
                print("#", end=" ")
            else:
                if M[i][j] == 0:
                    print("  ", end=" ")
                else:
                    print(M[i][j], end=" ")
        print()


def mazeSolver(maze, n):
    end = (n - 1, n - 1)
    moves = ((0, 1), (1, 0), (0, -1), (-1, 0))
    queue, costs = [(0, 0)], {(0, 0): 0}

    visited = set()
    while queue:
        token = queue.pop(0)
        x, y = token[0], token[1]
        if token == end:  # Goal reached
            return costs[token] # Return shortest path cost

        if token not in visited:
            visited.add(token)
            for dx, dy in moves: # Check all possible moves
                new_x = x + dx * maze[x][y]  # New move in x direction
                new_y = y + dy * maze[x][y]  # New move in y direction
                if 0 <= new_x < n and 0 <= new_y < n: # Check if new move is valid
                    if maze[new_x][new_y] != 0:  # Ignore 0s
                        next = (new_x, new_y)  # Next token location
                        if (next not in costs or costs[next] > costs[token] + 1):  # Better cost exists
                            costs[next] = costs[token] + 1
                            queue.append(next)
    return -1


def main():

    path = os.getcwd() + "\\tests\\"
    testdir = os.listdir(path)
    tests = [f for f in testdir if re.match(r"test.*\.txt", f)]

    for test in tests:
        temp = path + test
        print("Running: ", test)
        with open(temp) as data:
            A = [eval(s.strip()) for s in data.readlines()]
            n = A[0]
            A = A[1:]
            M = [A[i: i + n] for i in range(0, len(A), n)]
            move_cost = mazeSolver(M, n)
            if move_cost == -1:
                print("Output: No Solution")
            else:
                print("Output: ", move_cost)


if __name__ == "__main__":
    main()
