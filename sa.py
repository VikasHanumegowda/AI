from collections import deque
from copy import deepcopy
import time
import random

if __name__ == "__main__":

    def print_matrix(matrix):
        for eachrow in matrix:
            for eachcolumn in eachrow:
                print(eachcolumn, end=' ')
            print()


    def print_output(matrix):
        for eachrow in matrix:
            for eachcolumn in eachrow:
                if eachcolumn == 'T':
                    print(2, end=' ')
                elif eachcolumn == 'Q':
                    print(1, end=' ')
                else:
                    print(0, end=' ')
            print()


    def rotate(matrix, degree):
        if abs(degree) not in [0, 90, 180, 270, 360]:
            # raise error or just return nothing or original
            pass
        if degree == 0:
            return list(matrix)
        elif degree > 0:
            return rotate(list(zip(*matrix[::-1])), degree - 90)
        else:
            return rotate(list(zip(*matrix)[::-1]), degree + 90)


    def mark_conflicts(row, col, matrix):
        for x in range(col, -1, -1):  # leftside
            if matrix[row][x] == 'T':
                break
            if type(matrix[row][x]) != str and x != col:  # to sides
                matrix[row][x] += 1
        for x in range(col, n):  # rightside
            if matrix[row][x] == 'T':
                break
            if type(matrix[row][x]) != str and x != col:
                matrix[row][x] += 1
        for x in range(row, -1, -1):  # top
            if matrix[x][col] == 'T':
                break
            if type(matrix[x][col]) != str and x != row:
                matrix[x][col] += 1
        for x in range(row, n):  # bottom
            if matrix[x][col] == 'T':
                break
            if type(matrix[x][col]) != str and x != row:
                matrix[x][col] += 1
        x, y = col, row
        while n > x >= 0 and n > y >= 0:  # to lower-left end
            if matrix[y][x] == 'T':
                break
            if type(matrix[y][x]) == int:
                matrix[y][x] += 1
            y += 1
            x -= 1
        x, y = col, row
        while n > x >= 0 and n > y >= 0:  # to upper-right end
            if matrix[y][x] == 'T':
                break
            if type(matrix[y][x]) == int:
                matrix[y][x] += 1
            y -= 1
            x += 1
        x, y = col, row
        while n > x >= 0 and n > y >= 0:  # to upper-left end
            if matrix[y][x] == 'T':
                break
            if type(matrix[y][x]) == int:
                matrix[y][x] += 1
            y -= 1
            x -= 1
        x, y = col, row
        while n > x >= 0 and n > y >= 0:  # to lower-right end
            if matrix[y][x] == 'T':
                break
            if type(matrix[y][x]) == int:
                matrix[y][x] += 1
            y += 1
            x += 1
        return deepcopy(matrix)


    def find_possible_children(row, n, matrix, q, nqueens1):
        propagation = 0
        if row < n - 1:
            for y in range(row, n):
                for x in range(n):
                    if y < n:
                        if matrix[y][x] == 0:
                            propagation = 1
                            q.append(tuple([y, x, deepcopy(matrix), nqueens1]))
                if propagation != 0:
                    break
        return q


    def sa(board, n, p, *args):
        # T = time.
        board = []
        for x in range(n):
            # for

        pass


    f = open("input.txt", "r")
    bfs_dfs = f.readline().strip()  # for the first line retrieval
    print(bfs_dfs)
    n = int(f.readline().strip())  # Size of square board
    p = int(f.readline().strip())  # Number of Queens
    matrix1 = []
    for x in range(n):
        matrix1.append([int(x) if x == '0' else 'T' for x in f.readline().strip()])
    start = time.time()
    q1 = deque()
    numberq = []
    found = 0
    output = open("output.txt", "w")

    end = time.time()
    print("time : " + str(end - start))
