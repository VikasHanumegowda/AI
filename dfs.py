from collections import deque
import time

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


    def mark_conflicts(row, col, matrix):
        for x in range(col, -1, -1):  # leftside
            if matrix[row][x] == 'T':
                break
            if type(matrix[row][x]) != str and x != col:  # to sides
                matrix[row][x] += 1
        # for x in range(col,n)
        for x in range(col, n):  # rightside
            if matrix[row][x] == 'T':
                break
            if type(matrix[row][x]) != str and x != col:  # top-bottom
                matrix[row][x] += 1

        for x in range(row, -1, -1):  # top
            if matrix[x][col] == 'T':
                break
            if type(matrix[x][col]) != str and x != row:  # to sides
                matrix[x][col] += 1
        # for x in range(col,n)
        for x in range(row, n):  # bottom
            if matrix[x][col] == 'T':
                break
            if type(matrix[x][col]) != str and x != row:  # top-bottom
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

        return [[x for x in y] for y in matrix]


    def find_possible_children(row, n, matrix, q, nqueens1):
        propagation = 0
        if row < n - 1:
            for y in range(row, n):
                for x in range(n):
                    if y < n:
                        if matrix[y][x] == 0:
                            propagation = 1
                            q.append(tuple([y, x, [[yy for yy in xx] for xx in matrix], nqueens1]))
                if propagation != 0:
                    break
        return q


    def dfs(q, p):
        if p == 0:
            return p
        queens_ret = 0
        while len(q) > 0:
            row, col, matrix, nqueens1 = q.pop()

            if matrix[row][col] == 0:
                matrix[row][col] = 'Q'
                nqueens1 += 1

                matrix = [[row for row in col] for col in mark_conflicts(row, col, matrix)]
                print()

                if nqueens1 == p:
                    print("OK")
                    # print_output(matrix)
                    return nqueens1

                q = [i for i in find_possible_children(row, n, matrix, q, nqueens1)]

                if row == n - 1:
                    if nqueens1 < p:
                        for x in range(n):
                            for y in range(n):
                                if matrix[x][y] == 0:
                                    nqueens1 += 1
                                    matrix[x][y] = 'Q'
                                    matrix = [[row for row in col] for col in mark_conflicts(x, y, matrix)]
                                    # print_matrix(matrix)
                                    # print([x[:2] for x in q])
                                    # print
                                    if nqueens1 == p:
                                        print("OK")
                                        # print_output(matrix)
                                        return nqueens1
                                    q = [i for i in find_possible_children(row, n, matrix, q, nqueens1)]

                queens_ret = nqueens1
                # print_matrix(matrix)
                # print([x[:2] for x in q])
                # print()

            if queens_ret == p:
                print("OK")
                # print_output(matrix)
                return queens_ret
                # for x in matrixreturn -1
            # print_matrix(matrix)
            # print([x[:2] for x in q])
            # print()
        return -1


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

    f = open("input.txt", "r")
    f.readline()  # for the first line retrieval
    n = int(f.readline().strip())  # Size of square board
    p = int(f.readline().strip())  # Number of Queens
    # print(n)
    # n vs p check (TO BE DONE)
    start = time.time()
    q1 = deque()

    # matrix1 = [[0 for x in range(n)] for x in range(n)]
    matrix1 = []
    for x in range(n):
        matrix1.append([int(x) if x == '0' else 'T' for x in f.readline().strip()])
    # for eachrow in matrix1:
    #     for eachcolumn in eachrow:
    #         print(eachcolumn, end=' ')
    #     print()
    # for x in range(4):
    numberq = []
    for x in range(4):
        matrix1 = [[x for x in y] for y in rotate(matrix1, 90)]
        print_matrix(matrix1)
        print(x+1)
        for x in range(n):  # first column possible positions of Q
            if matrix1[0][x] == 0:
                q1.append(tuple([0, x, [[y for y in xx] for xx in matrix1], 0]))

        nqueens1 = 0

        numberq.append(dfs(q1, p))
        if any([x != -1 for x in numberq]):
            print("OK")
        # print(numberq)
        if numberq == -1:
            print("Failure")

    end = time.time()

    print("time : " + str(end - start))
