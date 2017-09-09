from collections import deque
import time

if __name__ == "__main__":
    f = open("input.txt", "r")
    f.readline()  # for the first line retrieval
    n = int(f.readline().strip())  # Size of square board
    p = int(f.readline().strip())  # Number of Queens

    # n vs p check (TO BE DONE)
    start = time.time()
    q1 = deque()

    matrix1 = [[0 for x in range(n)] for x in range(n)]

    for x in range(n):  # first column possible positions of Q
        q1.append(tuple([0, x, [[y for y in xx] for xx in matrix1], 0]))

    nqueens1 = 0


    def print_matrix(matrix):
        for eachrow in matrix:
            for eachcolumn in eachrow:
                print(eachcolumn, end=' ')
            print()


    def dfs(q, p):

        while len(q) > 0:
            row, col, matrix, nqueens1 = q.pop()

            matrix[row][col] = 'Q'
            nqueens1 += 1

            for x in range(n):  # to sides
                if type(matrix[row][x]) != str and x != col:
                    matrix[row][x] += 1
                if type(matrix[x][col]) != str and x != row:
                    matrix[x][col] += 1

            x, y = col, row

            while n > x >= 0 and n > y >= 0:  # to lower-left end
                if type(matrix[y][x]) == int:
                    matrix[y][x] += 1
                y += 1
                x -= 1

            x, y = col, row
            while n > x >= 0 and n > y >= 0:  # to upper-right end
                if type(matrix[y][x]) == int:
                    matrix[y][x] += 1
                y -= 1
                x += 1

            x, y = col, row
            while n > x >= 0 and n > y >= 0:  # to upper-left end
                if type(matrix[y][x]) == int:
                    matrix[y][x] += 1
                y -= 1
                x -= 1

            x, y = col, row
            while n > x >= 0 and n > y >= 0:  # to lower-right end
                if type(matrix[y][x]) == int:
                    matrix[y][x] += 1
                y += 1
                x += 1

            if row == n - 1:
                if nqueens1 != p:
                    print("No solutions")
                    continue
                else:
                    print("Success")
                    print_matrix(matrix)
                    return nqueens1

            propagation_possible = 0

            for x in range(n):  # append all 0 valued cells into Q
                if matrix[row + 1][x] == 0:
                    propagation_possible += 1
                    q.append(tuple([row + 1, x, [[y for y in xx] for xx in matrix], nqueens1]))

            if propagation_possible == 0:
                continue
                # print(nqueens1)
        return -1


    # print_matrix(matrix1)
    numberq = dfs(q1, p)

    if numberq == -1:
        print("Failure")

    end = time.time()

    print("time : " + str(end - start))
    # for y in matrix:
    #     for x in y:
    #         print(x,end=' ')
    #     print()
    # print(str(matrix)+"\n"+str(q))
