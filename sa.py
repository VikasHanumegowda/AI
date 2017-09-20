from collections import deque
from copy import deepcopy
import time
import random
import math

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


    def calculate_energy(board):
        sum1 = 0
        for x in board:
            for y in x:
                if type(y) == int:
                    sum1 += y
        return sum1


    def sa(n, p, board):
        start = time.time()
        emptyboard = deepcopy(board)
        prev_energy = -9999
        print_matrix(board)
        while (time.time() - start) < 280:
            count_of_q = 0
            board = deepcopy(emptyboard)
            while count_of_q < p:
                row = math.floor(random.random() * n)
                col = math.floor(random.random() * n)
                if board[row][col] != 'T' and board[row][col] != 'Q':
                    board[row][col] = 'Q'
                    board = mark_conflicts(row, col, board)
                    # print_matrix(board)
                    count_of_q += 1
                    # print()
                    # cur_energy = calculate_energy(board)
            new_energy = calculate_energy(board)
            print(new_energy)
            print_matrix(board)
            print()
            # if

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
    found = 0
    output = open("output.txt", "w")
    sa(n, p, matrix1)
    end = time.time()
    print("time : " + str(end - start))
