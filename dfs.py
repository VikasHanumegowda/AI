from collections import deque

if __name__ == "__main__":
    f = open("input.txt", "r")
    f.readline()  # for the first line retrieval
    n = int(f.readline().strip())  # Size of square board
    p = int(f.readline().strip())  # Number of Queens

    # n vs p check (TO BE DONE)

    q1 = deque()

    matrix1 = [[0 for x in range(n)] for x in range(n)]

    for x in range(n):  # first column possible positions of Q
        q1.append(tuple([0, x, matrix1]))

    nqueens1 = 0


    def print_matrix(matrix):
        for eachrow in matrix:
            for eachcolumn in eachrow:
                print(eachcolumn, end=' ')
            print()


    def dfs(q):

        while(len(q)>0):
            node = q.pop()

            row = node[0]
            col = node[1]
            matrix = node[2]

            print(row, col)
            matrix[row][col] = 'Q'
            nqueens += 1
            if nqueens == p:
                print("Success")
                return nqueens

            for x in range(n):  # to sides
                if type(matrix[row][x]) != str and x != col:
                    matrix[row][x] += 1

            for x in range(n):  # to top-bottom
                if type(matrix[x][col]) != str and x != row:
                    matrix[x][col] += 1

            x = col
            y = row
            while n > x >= 0 and n > y >= 0:  # to lower-left end
                if type(matrix[y][x]) == int:
                    matrix[y][x] += 1
                y += 1
                x -= 1

            x = col
            y = row
            while n > x >= 0 and n > y >= 0:  # to upper-right end
                if type(matrix[y][x]) == int:
                    matrix[y][x] += 1
                y -= 1
                x += 1

            x = col
            y = row
            while n > x >= 0 and n > y >= 0:  # to upper-left end
                if type(matrix[y][x]) == int:
                    matrix[y][x] += 1
                y -= 1
                x -= 1

            x = col
            y = row
            while n > x >= 0 and n > y >= 0:  # to lower-right end
                if type(matrix[y][x]) == int:
                    matrix[y][x] += 1
                y += 1
                x += 1

            print_matrix(matrix)

            propagation_possible = 0

            for x in range(n):  # append all 0 valued cells into Q
                if matrix[row + 1][x] == 0:
                    propagation_possible += 1
                    q.append(tuple([row + 1, x, matrix]))

            if propagation_possible == 0:
                continue

            print(q)
            if row == n - 1:
                if nqueens != p:
                    print("No solutions")
                    continue


    dfs(q1)

    if numberq == -1:
        print("Failure")
        # for y in matrix:
        #     for x in y:
        #         print(x,end=' ')
        #     print()
        # print(str(matrix)+"\n"+str(q))
