import math
import random
import time
from collections import deque
from contextlib import contextmanager
from copy import deepcopy


#
# class Timer:
#     def __enter__(self):
#         self.start = time.time()
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.end = time.time()
#         print("%30.20f" % (self.end - self.start))

@contextmanager
def my_timer():
    try:
        start = time.time()
        yield start
    finally:
        end = time.time()
        print("%020.15f" % (end - start))

if __name__ == "__main__":

    def print_matrix(matrix):
        for eachrow in matrix:
            for eachcolumn in eachrow:
                print(eachcolumn, end=' ')
            print()


    def print_output(matrix, f):
        for eachrow in matrix:
            for eachcolumn in eachrow:
                if eachcolumn == 'T':
                    f.write('2')
                elif eachcolumn == 'Q':
                    f.write('1')
                else:
                    f.write('0')
            f.write("\n")


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
            if not isinstance(matrix[row][x], str) and x != col:  # to sides
                matrix[row][x] += 1
        for x in range(col, n):  # rightside
            if matrix[row][x] == 'T':
                break
            if not isinstance(matrix[row][x], str) and x != col:
                matrix[row][x] += 1
        for x in range(row, -1, -1):  # top
            if matrix[x][col] == 'T':
                break
            if not isinstance(matrix[x][col], str) and x != row:
                matrix[x][col] += 1
        for x in range(row, n):  # bottom
            if matrix[x][col] == 'T':
                break
            if not isinstance(matrix[x][col], str) and x != row:
                matrix[x][col] += 1
        x, y = col, row
        while n > x >= 0 and n > y >= 0:  # to lower-left end
            if matrix[y][x] == 'T':
                break
            if isinstance(matrix[y][x], int):
                matrix[y][x] += 1
            y += 1
            x -= 1
        x, y = col, row
        while n > x >= 0 and n > y >= 0:  # to upper-right end
            if matrix[y][x] == 'T':
                break
            if isinstance(matrix[y][x], int):
                matrix[y][x] += 1
            y -= 1
            x += 1
        x, y = col, row
        while n > x >= 0 and n > y >= 0:  # to upper-left end
            if matrix[y][x] == 'T':
                break
            if isinstance(matrix[y][x], int):
                matrix[y][x] += 1
            y -= 1
            x -= 1
        x, y = col, row
        while n > x >= 0 and n > y >= 0:  # to lower-right end
            if matrix[y][x] == 'T':
                break
            if isinstance(matrix[y][x], int):
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


    def dfs(q, p):
        matrix = []
        if p == 0:
            return p, deepcopy(q.pop()[2])
        queens_ret = 0
        timeout = 0
        while q:
            if (time.time() - start) >= 280:
                timeout = 1
                break
            row, col, matrix, nqueens1 = q.pop()
            if matrix[row][col] == 0:
                matrix[row][col] = 'Q'
                nqueens1 += 1
                matrix = deepcopy(mark_conflicts(row, col, matrix))
                if nqueens1 == p:
                    return nqueens1, deepcopy(matrix)
                q = deepcopy(find_possible_children(row, n, matrix, q, nqueens1))
                if row == n - 1:
                    if nqueens1 < p:
                        for x in range(n):
                            for y in range(n):
                                if matrix[x][y] == 0:
                                    nqueens1 += 1
                                    matrix[x][y] = 'Q'
                                    matrix = deepcopy(mark_conflicts(x, y, matrix))
                                    if nqueens1 == p:
                                        return nqueens1, matrix
                                    q = deepcopy(find_possible_children(row, n, matrix, q, nqueens1))
                queens_ret = nqueens1
            if queens_ret == p:
                return queens_ret, matrix
        if timeout == 1:
            return -1, matrix
        return -1, matrix


    def bfs(q, p):
        matrix = []
        timeout = 0
        if p == 0:
            return p, deepcopy(q.pop()[2])
        queens_ret = 0
        while q:
            if (time.time() - start) >= 280:
                timeout = 1
                break
            row, col, matrix, nqueens1 = q.popleft()
            if matrix[row][col] == 0:
                matrix[row][col] = 'Q'
                nqueens1 += 1
                matrix = deepcopy(mark_conflicts(row, col, matrix))
                if nqueens1 == p:
                    return nqueens1, deepcopy(matrix)
                q = find_possible_children(row, n, matrix, q, nqueens1)
                if not q:
                    if nqueens1 < p:
                        for x in range(n):
                            for y in range(n):
                                if matrix[x][y] == 0:
                                    nqueens1 += 1
                                    matrix[x][y] = 'Q'
                                    matrix = deepcopy(mark_conflicts(x, y, matrix))
                                    if nqueens1 == p:
                                        return nqueens1, matrix
                                    q = deepcopy(find_possible_children(row, n, matrix, q, nqueens1))
                queens_ret = nqueens1
        if queens_ret == p:
            return queens_ret, matrix
        if timeout == 1:
            return -1, matrix
        return -1, matrix


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
        if r < p:
            return True
        return False


    def sa(n, p, board):
        start = time.time()
        emptyboard = deepcopy(board)
        tot_energy = 0
        list_of_pos = []
        while len(list_of_pos) != p:
            row = math.floor(random.random() * n)
            col = math.floor(random.random() * n)
            if board[row][col] != 'T' and board[row][col] != 'Q' and tuple([row, col]) not in list_of_pos:
                board[row][col] = 'Q'
                list_of_pos.append(tuple([row, col]))
        for x in list_of_pos:
            tot_energy += calc_energy(x[0], x[1], board)
        prev_energy = tot_energy
        nn = 1.05
        timeout = 0
        while True:
            if (time.time() - start) >= 280:
                timeout = 1
                break
            T = 1 / math.log(nn)
            nn += 1
            board = deepcopy(emptyboard)
            rand_pos = math.floor(random.random() * p)
            old_tup = list_of_pos.pop(rand_pos)
            row = random.randint(0, n - 1)
            col = random.randint(0, n - 1)
            new_tup = tuple([row, col])
            while new_tup in list_of_pos or not isinstance(board[row][col], int):
                row = random.randint(0, n - 1)
                col = random.randint(0, n - 1)
                new_tup = tuple([row, col])
            list_of_pos.append(new_tup)
            board = deepcopy(emptyboard)
            for x in list_of_pos:
                board[x[0]][x[1]] = 'Q'
            tot_energy = 0
            for x in list_of_pos:
                tot_energy += calc_energy(x[0], x[1], board)
            delta_energy = tot_energy - prev_energy
            if delta_energy < 0:  # continue to next state
                prev_energy = tot_energy
            else:
                if is_probable(math.exp(-delta_energy / T)):  # continue to next state
                    prev_energy = tot_energy
                else:
                    list_of_pos.append(old_tup)
                    list_of_pos.remove(new_tup)
            # print_matrix(board)
            if prev_energy == 0:
                break
                # print(list_of_pos)
                # print(len(list_of_pos))
                # print()
        if prev_energy == 0:
            return p, board
        if timeout == 1:
            return -1, board


    with open("input.txt", "r") as f:
        bfs_dfs = f.readline().strip()  # for the first line retrieval

        n = int(f.readline().strip())  # Size of square board
        p = int(f.readline().strip())  # Number of Queens

        matrix1 = []
        for x in range(n):
            matrix1.append([int(x) if x == '0' else 'T' for x in f.readline().strip()])
        start = time.time()
        # with Timer():
        with my_timer():
            q1 = deque()
            numberq = []
            found = 0
            with open("output.txt", "w") as output:
                for x in range(2):
                    matrix1 = [[i for i in j] for j in rotate(matrix1, 90)]  # rotate matrix and process

                    for xx in range(n):  # first column possible positions of Q
                        if matrix1[0][xx] == 0:
                            q1.append(tuple([0, xx, deepcopy(matrix1), 0]))
                    nqueens1 = 0

                    if bfs_dfs == "DFS":
                        ret_nq, matrix = dfs(q1, p)
                    elif bfs_dfs == "BFS":
                        ret_nq, matrix = bfs(q1, p)
                    elif bfs_dfs == "SA":
                        ret_nq, matrix = sa(n, p, matrix1)

                    if x == 0:
                        matrix = deepcopy(rotate(matrix, 270))
                    elif x == 1:
                        matrix = deepcopy(rotate(matrix, 180))

                    if ret_nq == p:
                        output.write("OK\n")
                        print_output(matrix, output)
                        found = 1
                        break

                    numberq.append([ret_nq, matrix])

                    if bfs_dfs == "SA":
                        break
                if found == 0:
                    if all([xx[0] == -1 for xx in numberq]):
                        output.write("FAIL\n")
                # end = time.time()
