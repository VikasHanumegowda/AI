from collections import deque
from copy import deepcopy
import time
import multiprocessing

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
                    output.write('2')
                elif eachcolumn == 'Q':
                    output.write('1')
                else:
                    output.write('0')
            output.write("\n")
        output.write("\n")


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


    def dfs(q, p):
        if p == 0:
            return p, deepcopy(q.pop()[2])
        queens_ret = 0
        while len(q) > 0:
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
        return -1, matrix


    def bfs(q, p):
        if p == 0:
            return p, deepcopy(q.pop()[2])
        queens_ret = 0
        while len(q) > 0:
            row, col, matrix, nqueens1 = q.popleft()
            if matrix[row][col] == 0:
                matrix[row][col] = 'Q'
                nqueens1 += 1
                matrix = deepcopy(mark_conflicts(row, col, matrix))
                if nqueens1 == p:
                    return nqueens1, deepcopy(matrix)
                q = find_possible_children(row, n, matrix, q, nqueens1)
                if len(q) == 0:
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
        return -1, matrix


    def sa():

        pass



    for xx in range(4):
        if xx == 0:
            f = open("input.txt", "r")
        else:
            f = open("input"+str(xx)+".txt", "r")
        bfs_dfs = f.readline().strip()  # for the first line retrieval
        # print(bfs_dfs)
        n = int(f.readline().strip())  # Size of square board
        p = int(f.readline().strip())  # Number of Queens
        matrix1 = []
        for x in range(n):
            matrix1.append([int(x) if x == '0' else 'T' for x in f.readline().strip()])
        start = time.time()
        q1 = deque()
        numberq = []
        found = 0
        output = open("output"+str(xx)+".txt", "w")
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
                ret_nq, matrix = bfs(q1, p)
            if x == 0:
                # print(x + 1)
                matrix = deepcopy(rotate(matrix, 270))

            elif x == 1:
                # print(x + 1)
                matrix = deepcopy(rotate(matrix, 180))
            if ret_nq == p:
                print("OK")
                output.write("OK\n")

                print_output(matrix, output)
                found = 1
                break
                print()

            numberq.append([ret_nq, matrix])

        if found == 0:
            if all([xx[0] == -1 for xx in numberq]):
                print("FAIL")
                output.write("FAIL\n")
        end = time.time()
        output.close()
        f.close()
        print("time : " + str(end - start))
