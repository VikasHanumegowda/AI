from collections import OrderedDict, Counter
from copy import deepcopy
from time import time


def print_matrix(matrix):
    for eachrow in matrix:
        for eachcolumn in eachrow:
            print("[ ", end='')
            for eachelement in eachcolumn:
                print(eachelement, end=' ')
            print("] ,", end='')
        print()


def print_output(matrix, f):
    for eachrow in matrix:
        for eachcolumn in eachrow:
            f.write(str(eachcolumn[0]))
        f.write("\n")


def calculate_connectivity(matrix, x, y, n):
    # matrix = [cellvalue, visited, sumvalue]
    # return x-coord, y-coord, sumvalue, matrix

    if x == y == 0 and n == 1:
        return x, y, matrix[x][y][0], deepcopy(matrix)
    matrix[x][y][1] = 1
    if x == 0:
        if y == 0:
            # top-left
            if matrix[x][y + 1][0] == matrix[x][y][0] and matrix[x][y + 1][1] == 0:
                r1, r2, a, matrix = calculate_connectivity(matrix, x, y + 1, n)
                matrix[x][y][2] += a
            if matrix[x + 1][y][0] == matrix[x][y][0] and matrix[x + 1][y][1] == 0:
                r1, r2, a, matrix = calculate_connectivity(matrix, x + 1, y, n)
                matrix[x][y][2] += a
        elif y == n - 1:
            # top-right
            if matrix[x][y - 1][0] == matrix[x][y][0] and matrix[x][y - 1][1] == 0:
                r1, r2, a, matrix = calculate_connectivity(matrix, x, y - 1, n)
                matrix[x][y][2] += a
            if matrix[x + 1][y][0] == matrix[x][y][0] and matrix[x + 1][y][1] == 0:
                r1, r2, a, matrix = calculate_connectivity(matrix, x + 1, y, n)
                matrix[x][y][2] += a
        else:
            # top-row
            if matrix[x][y + 1][0] == matrix[x][y][0] and matrix[x][y + 1][1] == 0:
                r1, r2, a, matrix = calculate_connectivity(matrix, x, y + 1, n)
                matrix[x][y][2] += a
            if matrix[x][y - 1][0] == matrix[x][y][0] and matrix[x][y - 1][1] == 0:
                r1, r2, a, matrix = calculate_connectivity(matrix, x, y - 1, n)
                matrix[x][y][2] += a
            if matrix[x + 1][y][0] == matrix[x][y][0] and matrix[x + 1][y][1] == 0:
                r1, r2, a, matrix = calculate_connectivity(matrix, x + 1, y, n)
                matrix[x][y][2] += a
    elif x == n - 1:
        if y == 0:
            # bottom-left
            if matrix[x][y + 1][0] == matrix[x][y][0] and matrix[x][y + 1][1] == 0:
                r1, r2, a, matrix = calculate_connectivity(matrix, x, y + 1, n)
                matrix[x][y][2] += a
            if matrix[x - 1][y][0] == matrix[x][y][0] and matrix[x - 1][y][1] == 0:
                r1, r2, a, matrix = calculate_connectivity(matrix, x - 1, y, n)
                matrix[x][y][2] += a
        elif y == n - 1:
            # bottom-right
            if matrix[x][y - 1][0] == matrix[x][y][0] and matrix[x][y - 1][1] == 0:
                r1, r2, a, matrix = calculate_connectivity(matrix, x, y - 1, n)
                matrix[x][y][2] += a
            if matrix[x - 1][y][0] == matrix[x][y][0] and matrix[x - 1][y][1] == 0:
                r1, r2, a, matrix = calculate_connectivity(matrix, x - 1, y, n)
                matrix[x][y][2] += a
        else:
            # bottom-row
            if matrix[x][y + 1][0] == matrix[x][y][0] and matrix[x][y + 1][1] == 0:
                r1, r2, a, matrix = calculate_connectivity(matrix, x, y + 1, n)
                matrix[x][y][2] += a
            if matrix[x][y - 1][0] == matrix[x][y][0] and matrix[x][y - 1][1] == 0:
                r1, r2, a, matrix = calculate_connectivity(matrix, x, y - 1, n)
                matrix[x][y][2] += a
            if matrix[x - 1][y][0] == matrix[x][y][0] and matrix[x - 1][y][1] == 0:
                r1, r2, a, matrix = calculate_connectivity(matrix, x - 1, y, n)
                matrix[x][y][2] += a
    else:
        if y == 0:
            # middle-left
            if matrix[x][y + 1][0] == matrix[x][y][0] and matrix[x][y + 1][1] == 0:
                r1, r2, a, matrix = calculate_connectivity(matrix, x, y + 1, n)
                matrix[x][y][2] += a
            if matrix[x - 1][y][0] == matrix[x][y][0] and matrix[x - 1][y][1] == 0:
                r1, r2, a, matrix = calculate_connectivity(matrix, x - 1, y, n)
                matrix[x][y][2] += a
            if matrix[x + 1][y][0] == matrix[x][y][0] and matrix[x + 1][y][1] == 0:
                r1, r2, a, matrix = calculate_connectivity(matrix, x + 1, y, n)
                matrix[x][y][2] += a
        elif y == n - 1:
            # middle-right
            if matrix[x][y - 1][0] == matrix[x][y][0] and matrix[x][y - 1][1] == 0:
                r1, r2, a, matrix = calculate_connectivity(matrix, x, y - 1, n)
                matrix[x][y][2] += a
            if matrix[x - 1][y][0] == matrix[x][y][0] and matrix[x - 1][y][1] == 0:
                r1, r2, a, matrix = calculate_connectivity(matrix, x - 1, y, n)
                matrix[x][y][2] += a
            if matrix[x + 1][y][0] == matrix[x][y][0] and matrix[x + 1][y][1] == 0:
                r1, r2, a, matrix = calculate_connectivity(matrix, x + 1, y, n)
                matrix[x][y][2] += a
        else:
            # middle-middle :-p
            if matrix[x][y - 1][0] == matrix[x][y][0] and matrix[x][y - 1][1] == 0:
                r1, r2, a, matrix = calculate_connectivity(matrix, x, y - 1, n)
                matrix[x][y][2] += a
            if matrix[x][y + 1][0] == matrix[x][y][0] and matrix[x][y + 1][1] == 0:
                r1, r2, a, matrix = calculate_connectivity(matrix, x, y + 1, n)
                matrix[x][y][2] += a
            if matrix[x - 1][y][0] == matrix[x][y][0] and matrix[x - 1][y][1] == 0:
                r1, r2, a, matrix = calculate_connectivity(matrix, x - 1, y, n)
                matrix[x][y][2] += a
            if matrix[x + 1][y][0] == matrix[x][y][0] and matrix[x + 1][y][1] == 0:
                r1, r2, a, matrix = calculate_connectivity(matrix, x + 1, y, n)
                matrix[x][y][2] += a

    return x, y, matrix[x][y][2], deepcopy(matrix)


def remove_fruits(matrix, x, y, n):
    # matrix = [cellvalue, visited, sumvalue]
    # return x-coord, y-coord, sumvalue, matrix

    found = 0
    if x == y == 0 and n == 1:
        matrix[x][y][0] = '*'
        return deepcopy(matrix)
    matrix[x][y][1] = 2
    if x == 0:
        if y == 0:
            # top-left
            if matrix[x][y + 1][0] == matrix[x][y][0] and matrix[x][y + 1][1] == 1:
                matrix = remove_fruits(matrix, x, y + 1, n)
                found = 1
            if matrix[x + 1][y][0] == matrix[x][y][0] and matrix[x + 1][y][1] == 1:
                matrix = remove_fruits(matrix, x + 1, y, n)
                found = 1
        elif y == n - 1:
            # top-right
            if matrix[x][y - 1][0] == matrix[x][y][0] and matrix[x][y - 1][1] == 1:
                matrix = remove_fruits(matrix, x, y - 1, n)
                found = 1
            if matrix[x + 1][y][0] == matrix[x][y][0] and matrix[x + 1][y][1] == 1:
                matrix = remove_fruits(matrix, x + 1, y, n)
                found = 1
        else:
            # top-row
            if matrix[x][y + 1][0] == matrix[x][y][0] and matrix[x][y + 1][1] == 1:
                matrix = remove_fruits(matrix, x, y + 1, n)
                found = 1
            if matrix[x][y - 1][0] == matrix[x][y][0] and matrix[x][y - 1][1] == 1:
                matrix = remove_fruits(matrix, x, y - 1, n)
                found = 1
            if matrix[x + 1][y][0] == matrix[x][y][0] and matrix[x + 1][y][1] == 1:
                matrix = remove_fruits(matrix, x + 1, y, n)
                found = 1
    elif x == n - 1:
        if y == 0:
            # bottom-left
            if matrix[x][y + 1][0] == matrix[x][y][0] and matrix[x][y + 1][1] == 1:
                matrix = remove_fruits(matrix, x, y + 1, n)
                found = 1
            if matrix[x - 1][y][0] == matrix[x][y][0] and matrix[x - 1][y][1] == 1:
                matrix = remove_fruits(matrix, x - 1, y, n)
                found = 1
        elif y == n - 1:
            # bottom-right
            if matrix[x][y - 1][0] == matrix[x][y][0] and matrix[x][y - 1][1] == 1:
                matrix = remove_fruits(matrix, x, y - 1, n)
                found = 1
            if matrix[x - 1][y][0] == matrix[x][y][0] and matrix[x - 1][y][1] == 1:
                matrix = remove_fruits(matrix, x - 1, y, n)
                found = 1
        else:
            # bottom-row
            if matrix[x][y + 1][0] == matrix[x][y][0] and matrix[x][y + 1][1] == 1:
                matrix = remove_fruits(matrix, x, y + 1, n)
                found = 1
            if matrix[x][y - 1][0] == matrix[x][y][0] and matrix[x][y - 1][1] == 1:
                matrix = remove_fruits(matrix, x, y - 1, n)
                found = 1
            if matrix[x - 1][y][0] == matrix[x][y][0] and matrix[x - 1][y][1] == 1:
                matrix = remove_fruits(matrix, x - 1, y, n)
                found = 1
    else:
        if y == 0:
            # middle-left
            if matrix[x][y + 1][0] == matrix[x][y][0] and matrix[x][y + 1][1] == 1:
                matrix = remove_fruits(matrix, x, y + 1, n)
                found = 1
            if matrix[x - 1][y][0] == matrix[x][y][0] and matrix[x - 1][y][1] == 1:
                matrix = remove_fruits(matrix, x - 1, y, n)
                found = 1
            if matrix[x + 1][y][0] == matrix[x][y][0] and matrix[x + 1][y][1] == 1:
                matrix = remove_fruits(matrix, x + 1, y, n)
                found = 1
        elif y == n - 1:
            # middle-right
            if matrix[x][y - 1][0] == matrix[x][y][0] and matrix[x][y - 1][1] == 1:
                matrix = remove_fruits(matrix, x, y - 1, n)
                found = 1
            if matrix[x - 1][y][0] == matrix[x][y][0] and matrix[x - 1][y][1] == 1:
                matrix = remove_fruits(matrix, x - 1, y, n)
                found = 1
            if matrix[x + 1][y][0] == matrix[x][y][0] and matrix[x + 1][y][1] == 1:
                matrix = remove_fruits(matrix, x + 1, y, n)
                found = 1
        else:
            # middle-middle :-p
            if matrix[x][y - 1][0] == matrix[x][y][0] and matrix[x][y - 1][1] == 1:
                matrix = remove_fruits(matrix, x, y - 1, n)
                found = 1
            if matrix[x][y + 1][0] == matrix[x][y][0] and matrix[x][y + 1][1] == 1:
                matrix = remove_fruits(matrix, x, y + 1, n)
                found = 1
            if matrix[x - 1][y][0] == matrix[x][y][0] and matrix[x - 1][y][1] == 1:
                matrix = remove_fruits(matrix, x - 1, y, n)
                found = 1
            if matrix[x + 1][y][0] == matrix[x][y][0] and matrix[x + 1][y][1] == 1:
                matrix = remove_fruits(matrix, x + 1, y, n)
                found = 1

    if found == 1:
        matrix[x][y][0] = '*'
        return deepcopy(matrix)
    else:
        matrix[x][y][0] = '*'
        return deepcopy(matrix)


def max_level():
    pass


def min_level():
    pass


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


def index_of_star(row):
    pass


def apply_gravity(grav_matrix):
    n = len(grav_matrix)
    grav_matrix = rotate(grav_matrix, 270)
    matrix1 = []
    for x in range(n):
        temp = []
        for y in range(n):
            temp.append(grav_matrix[x][y])
        matrix1.append(temp)
    # print_matrix(matrix1)
    for row in matrix1:
        c = Counter([e[0] for e in row])
        if c['*'] == 0:
            continue
        else:
            row.reverse()
            # i = 0
            count = 0
            while count < c['*']:
                for x in range(n):
                    if row[x][0] == '*':
                        break
                aa = row.pop(x)
                row.append(aa)
                count += 1
                # i+=1
            row.reverse()
    matrix1 = rotate(matrix1, 90)
    return deepcopy(matrix1)


def my_game(n, matrix, dict_fruit, depth):
    # matrix = [cellvalue, visited, sumvalue]
    # dictfruit = {0 : [max_value, x-coord, y-coord,matrix]}
    state_stack = OrderedDict()
    if depth == 5:
        return 0  # ?  ?
    for x in range(n):
        for y in range(n):
            if matrix[x][y][0] != '*':
                x1, y1, z, matrix1 = calculate_connectivity(matrix, x, y, n)
                if z > dict_fruit[matrix[x][y][0]][0]:
                    dict_fruit[matrix[x][y][0]][0] = z
                    dict_fruit[matrix[x][y][0]][1] = x1
                    dict_fruit[matrix[x][y][0]][2] = y1
    dict_fruit = OrderedDict(reversed(sorted(dict_fruit.items(), key=lambda h: h[1][0])))

    fruit_to_remove = []
    fruit_to_remove.append(dict_fruit.popitem(False))
    fruit_to_remove.append(dict_fruit.popitem(False))
    print(fruit_to_remove)
    # for i in range(2):
    matrix = remove_fruits(matrix, fruit_to_remove[0][1][1], fruit_to_remove[0][1][2], n)
    matrix = apply_gravity(matrix)

    state_stack[depth] = [dict_fruit, matrix]
    xcoor = fruit_to_remove[0][1][1]
    ycoor = fruit_to_remove[0][1][2]

    output = open("output.txt", "w")
    output.write(chr(ord('A') + ycoor))
    output.write(str(1 + xcoor))
    output.write("\n")
    print_output(matrix,output)
    output.close()
    return fruit_to_remove[0][1][0]


if __name__ == "__main__":
    # matrix = [cellvalue, visited, sumvalue]
    # dictfruit = {0 : [max_value, x-coord, y-coord]}

    f = open("input.txt", "r")
    n = int(f.readline().strip())
    p = int(f.readline().strip())
    t = float(f.readline().strip())

    dict_fruit = {x: [0, -1, -1] for x in range(p)}
    dict_fruit = OrderedDict(dict_fruit)
    matrix = []
    for i in range(n):
        line = []
        for x in f.readline().strip():
            if x.isdigit():
                line.append([int(x), 0, 1])
            else:
                line.append([x, 0, 1])
        matrix.append(line)
    empty = deepcopy(matrix)
    start = time()
    print(my_game(n, empty, dict_fruit, 0))
    stop = time()
    print(stop - start)
