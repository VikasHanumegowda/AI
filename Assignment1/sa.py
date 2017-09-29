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


    def calc_energy(row, col, matrix):
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
            if matrix[y][x] == 'T':
                break
            if matrix[y][x] == 'Q' and x != col and y != row:
                c += 1
            y += 1
            x -= 1
        x, y = col, row
        while n > x >= 0 and n > y >= 0:  # to upper-right end
            if matrix[y][x] == 'T':
                break
            if matrix[y][x] == 'Q' and x != col and y != row:
                c += 1
            y -= 1
            x += 1
        x, y = col, row
        while n > x >= 0 and n > y >= 0:  # to upper-left end
            if matrix[y][x] == 'T':
                break
            if matrix[y][x] == 'Q' and x != col and y != row:
                c += 1
            y -= 1
            x -= 1
        x, y = col, row
        while n > x >= 0 and n > y >= 0:  # to lower-right end
            if matrix[y][x] == 'T':
                break
            if matrix[y][x] == 'Q' and x != col and y != row:
                c += 1
            y += 1
            x += 1
        return c


    def is_probable(p):
        r = random.random()
        # print(r, p)
        if r < p:
            return True
        return False


    def sa(n, p, board):
        start = time.time()
        emptyboard = deepcopy(board)
        tot_energy = 0
        count_of_q = 0
        list_of_pos = []
        while count_of_q < p:
            row = math.floor(random.random() * n)
            col = math.floor(random.random() * n)
            if board[row][col] != 'T' and board[row][col] != 'Q':
                board[row][col] = 'Q'
                list_of_pos.append(tuple([row, col]))
                count_of_q += 1
        for x in range(p):
            # print_matrix(board)
            tot_energy += calc_energy(list_of_pos[x][0], list_of_pos[x][1], board)
        prev_energy = tot_energy
        nn = 1.05
        # delta_energy = -99
        while (time.time() - start) < 280 and prev_energy != 0:
            T = 1 / math.log(nn)
            nn += 1
            # print(time.time() - start, T)
            board = deepcopy(emptyboard)
            rand_pos = math.floor(random.random() * p)
            old_tup = list_of_pos.pop(rand_pos)
            # row = math.floor(random.random() * n)
            # col = math.floor(random.random() * n)
            row = random.randint(0, n - 1)
            col = random.randint(0, n - 1)
            new_tup = tuple([row, col])
            while new_tup in list_of_pos and type(board[row][col]) != int:
                row = random.randint(0, n - 1)
                col = random.randint(0, n - 1)
                new_tup = tuple([row, col])

            list_of_pos.append(new_tup)

            for x in list_of_pos:
                board[x[0]][x[1]] = 'Q'
            tot_energy = 0
            for x in range(p):
                tot_energy += calc_energy(list_of_pos[x][0], list_of_pos[x][1], board)
            # print(list_of_pos, tot_energy)
            delta_energy = tot_energy - prev_energy
            if delta_energy < 0:  # continue to next state
                prev_energy = tot_energy
            # else:
            #     list_of_pos.append(old_tup)
            #     list_of_pos.remove(new_tup)
            # print(time.time()-start)
            else:
                # print(delta_energy)
                # print(T, math.exp(-delta_energy / T))
                if is_probable(math.exp(-delta_energy / T)):  # continue to next state
                    prev_energy = tot_energy
                else:
                    list_of_pos.append(old_tup)
                    list_of_pos.remove(new_tup)

            # print(tot_energy, len(list_of_pos))
            # print(list_of_pos)
            # print_matrix(board)
            # print()
        # print_matrix(board)
        # print("time" + str(time.time() - start))


    f = open("input3.txt", "r")
    bfs_dfs = f.readline().strip()  # for the first line retrieval
    print(bfs_dfs)
    n = int(f.readline().strip())  # Size of square board
    p = int(f.readline().strip())  # Number of Queens
    matrix1 = []
    for y in range(n):
        matrix1.append([int(x) if x == '0' else 'T' for x in f.readline().strip()])
    start = time.time()
    q1 = deque()
    found = 0
    output = open("output.txt", "w")
    sa(n, p, matrix1)
    end = time.time()
    print("time : " + str(end - start))
