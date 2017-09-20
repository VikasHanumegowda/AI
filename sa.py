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


    def calc_conflicts(row, col, matrix):
        c = 0
        for x in range(col, -1, -1):  # leftside
            if matrix[row][x] == 'T':
                break
            if matrix[row][x] == 'Q' and x != col:  # to sides
                c += 1
        for x in range(col, n):  # rightside
            if matrix[row][x] == 'T':
                break
            if matrix[row][x] == 'Q' and x != col:
                c += 1
        for x in range(row, -1, -1):  # top
            if matrix[x][col] == 'T':
                break
            if matrix[x][col] == 'Q' and x != row:
                c += 1
        for x in range(row, n):  # bottom
            if matrix[x][col] == 'T':
                break
            if matrix[x][col] == 'Q' and x != row:
                c += 1
        x, y = col, row
        while n > x >= 0 and n > y >= 0:  # to lower-left end
            if matrix[x][y] == 'T':
                break
            if matrix[x][y] == 'Q' and x != row and y != col:
                c += 1
            y += 1
            x -= 1
        x, y = col, row
        while n > x >= 0 and n > y >= 0:  # to upper-right end
            if matrix[x][y] == 'T':
                break
            if matrix[x][y] == 'Q' and x != row and y != col:
                c += 1
            y -= 1
            x += 1
        x, y = col, row
        while n > x >= 0 and n > y >= 0:  # to upper-left end
            if matrix[x][y] == 'T':
                break
            if matrix[x][y] == 'Q' and x != row and y != col:
                c += 1
            y -= 1
            x -= 1
        x, y = col, row
        while n > x >= 0 and n > y >= 0:  # to lower-right end
            if matrix[x][y] == 'T':
                break
            if matrix[x][y] == 'Q' and x != row and y != col:
                c += 1
            y += 1
            x += 1
        return c


    def sa(n, p, board):
        start = time.time()
        emptyboard = deepcopy(board)
        prev_energy = -9999
        print_matrix(board)
        tot_conf = 0
        while (time.time() - start) < 280 or tot_conf != 0:
            count_of_q = 0
            board = deepcopy(emptyboard)
            while count_of_q < p:
                row = math.floor(random.random() * n)
                col = math.floor(random.random() * n)
                if board[row][col] != 'T' and board[row][col] != 'Q':
                    board[row][col] = 'Q'
                    count_of_q += 1
            tot_conf = 0
            # print_matrix(board)
            for x in range(n):
                for y in range(n):
                    calc = 0
                    # print_matrix(board)
                    if board[x][y] == 'Q':
                        calc = calc_conflicts(x, y, board)
                    tot_conf += calc

            # print_matrix(board)
            print(tot_conf)
            # print()
        print_matrix(board)
        print("time" + str(time.time() - start))


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
