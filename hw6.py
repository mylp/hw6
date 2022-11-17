import os
import re
from time import time

def shortest_path(maze, n):
    end = (n - 1, n - 1)
    moves = ((0, 1), (1, 0), (0, -1), (-1, 0))
    queue, dist = [(0, 0)], {(0, 0): 0}

    visited = set()
    while queue:
        token = queue.pop(0)  # Get next token location
        (x, y) = token
        if token == end:  # Goal reached
            return dist[token]  # Return shortest path distance

        if token not in visited:
            visited.add(token)  # Mark as visited
            for dx, dy in moves:  # Check all possible moves
                new_x = x + dx * maze[x][y]  # New move in x direction
                new_y = y + dy * maze[x][y]  # New move in y direction
                if 0 <= new_x < n and 0 <= new_y < n:  # Check if new move is valid
                    if maze[new_x][new_y] != 0:  # Ignore 0 locations
                        next = (new_x, new_y)  # Next token location
                        # Undiscovered or better distance exists
                        if (next not in dist or dist[next] > dist[token] + 1):
                            dist[next] = dist[token] + 1  # Update distance
                            queue.append(next)  # Add to queue

    return -1  # Exuasted all possible moves and no solution found


def main():

    # Read input file
    path = os.getcwd() + "\\tests\\"
    testdir = os.listdir(path)
    tests = None
    print("Enter \"sample\" to run sample test cases, \"test\" to run answer test cases, or nothing to run all test cases.")
    match input(""):
        case "sample":
            tests = [f for f in testdir if re.match(r"[^test].*\.txt", f)]
        case "test":
            tests = [f for f in testdir if re.match(r"test.*\.txt", f)]
        case _:
            tests = [f for f in testdir]
    print("\n")
    for test in tests:
        temp = path + test
        print("Running: ", test)
        with open(temp) as data:
            A = [eval(s.strip()) for s in data.readlines()]
            n = A[0]
            A = A[1:]
            M = [A[i: i + n] for i in range(0, len(A), n)]
            start_time = time()
            distance = shortest_path(M, n)
            duration = time() - start_time
            if distance == "-1":
                print("No solution found.")
                print("Runtime: "+str(duration*1000)+"ms\n")
            else:
                print("Shortest path distance: ", distance)
                print("Runtime: "+str(duration*1000)+"ms\n")


if __name__ == "__main__":
    main()
