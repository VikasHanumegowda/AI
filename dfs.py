from collections import deque
import time

if __name__ == "__main__":
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
    for x in range(n):  # first column possible positions of Q
        if matrix1[0][x] == 0:
            q1.append(tuple([0, x, [[y for y in xx] for xx in matrix1], 0]))

    nqueens1 = 0


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

        return matrix


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
                # print_matrix(matrix)
                print()
                # if row == n - 1:
                #     if nqueens1 != p:
                #         continue
                #     else:
                #         print_output(matrix)
                #         return nqueens1



                if nqueens1 == p:
                    print("OK")
                    print_output(matrix)
                    return nqueens1

                propagation = 0

                # for x in range(n):
                #     if row < n :
                #         if matrix[row + 1][x] == 0:
                #             propagation =1
                #             q.append(tuple([row + 1, x, [[y for y in xx] for xx in matrix], nqueens1]))

                for y in range(row + 1, n):
                    for x in range(n):
                        if y < n:
                            if matrix[y][x] == 0:
                                propagation = 1
                                q.append(tuple([y, x, [[yy for yy in xx] for xx in matrix], nqueens1]))
                    if propagation != 0:
                        break


                if row == n-1:
                    if nqueens1 < p:
                        for x in range(n):
                            for y in range(n):
                                if matrix[x][y] == 0:
                                    nqueens1 += 1
                                    matrix[x][y] = 'Q'
                                    matrix = [[row for row in col] for col in mark_conflicts(row, col, matrix)]
                                    if nqueens1 == p:
                                        # print("last")
                                        print_output(matrix)
                                        return nqueens1
                queens_ret = nqueens1
                print_matrix(matrix)
                print([x[:2] for x in q])
                print()
            if queens_ret == p:
                # print("last")
                # print_output(matrix)
                return queens_ret
                # for x in matrixreturn -1
        return -1


    # print_matrix(matrix1)
    numberq = dfs(q1, p)
    print(numberq)
    if numberq == -1:
        print("Failure")

    end = time.time()

    print("time : " + str(end - start))
    # for y in matrix:
    #     for x in y:
    #         print(x,end=' ')
    #     print()
    # print(str(matrix)+"\n"+str(q))
