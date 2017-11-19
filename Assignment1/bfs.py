from collections import deque
from copy import deepcopy
import time
import copy

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
                    # print(eachcolumn, end=' ')
            print()


    def rotate(matrix, degree):
        if abs(degree) not in [0, 90, 180, 270, 360]:
            pass
        # raise error or just return nothing or original
        if degree == 0:
            return matrix
        elif degree > 0:
            return rotate(zip(*matrix[::-1]), degree - 90)
        else:
            return rotate(zip(*matrix)[::-1], degree + 90)


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


    def find_possible_children(row, n, matrix_for_children, q, nqueens1):
        for x in reversed(range(n)):  # append all 0 valued cells into Q
            if matrix_for_children[row][x] == 0:
                q.insert(0, tuple([row, x, [[y for y in xx] for xx in matrix_for_children], nqueens1]))
            if row < n - 1:
                if matrix_for_children[row + 1][x] == 0:
                    q.insert(0, tuple([row + 1, x, [[y for y in xx] for xx in matrix_for_children], nqueens1]))
        return q


    f = open("inp.txt", "r")
    f.readline()  # for the first line retrieval
    n = int(f.readline().strip())  # Size of square board
    p = int(f.readline().strip())  # Number of Queens

    # n vs p check (TO BE DONE)
    matrix1 = []
    for x in range(n):  # generate state matrix
        matrix1.append([int(x) if x == '0' else 'T' for x in f.readline().strip()])

    q1 = deque()

    for x in range(n):  # first column possible positions of Q
        if matrix1[0][x] == 0:
            q1.insert(0, tuple([0, x, deepcopy(matrix1), 0]))

    nqueens1 = 0

    def bfs(q, p):
        if p == 0:
            return p, deepcopy(q.pop()[2])
        queens_ret = 0
        while len(q) > 0:
            row, col, matrix, nqueens1 = q.pop()
            if matrix[row][col] == 0:
                matrix[row][col] = 'Q'
                nqueens1 += 1

                matrix = deepcopy(mark_conflicts(row, col, matrix))
                print()

                if nqueens1 == p:
                    print("OK")
                    print_output(matrix)
                    return nqueens1, deepcopy(matrix)

                q = find_possible_children(row, n, matrix, q, nqueens1)

                print_matrix(matrix)

                if len(q) == 0:
                    if nqueens1 < p:
                        for x in range(n):
                            for y in range(n):
                                if matrix[x][y] == 0:
                                    nqueens1 += 1
                                    matrix[x][y] = 'Q'
                                    matrix = deepcopy(mark_conflicts(x, y, matrix))

                                    if nqueens1 == p:
                                        print("OK")
                                        print_output(matrix)
                                        return nqueens1, matrix
                                    q = deepcopy(find_possible_children(row, n, matrix, q, nqueens1))

                queens_ret = nqueens1

        if queens_ret == p:
            print("OK")
            print_output(matrix)
            return queens_ret, matrix

        return -1

    start = time.time()

    numberq, matrix = bfs(q1, p)
    print()
    print_matrix(matrix)
    if numberq == -1:
        print("FAIL")

    end = time.time()

    print("time : " + str(end - start))
