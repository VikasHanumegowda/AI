from collections import OrderedDict, Counter, deque
from copy import deepcopy
from time import time
from sys import maxsize
import math


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
        return x, y, matrix[x][y][2], deepcopy(matrix), matrix[x][y][0]
    matrix[x][y][1] = 1
    if x == 0:
        if y == 0:
            # top-left
            if matrix[x][y + 1][0] == matrix[x][y][0] and matrix[x][y + 1][1] == 0:
                r1, r2, a, matrix, d = calculate_connectivity(matrix, x, y + 1, n)
                matrix[x][y][2] += a
            if matrix[x + 1][y][0] == matrix[x][y][0] and matrix[x + 1][y][1] == 0:
                r1, r2, a, matrix, d = calculate_connectivity(matrix, x + 1, y, n)
                matrix[x][y][2] += a
        elif y == n - 1:
            # top-right
            if matrix[x][y - 1][0] == matrix[x][y][0] and matrix[x][y - 1][1] == 0:
                r1, r2, a, matrix, d = calculate_connectivity(matrix, x, y - 1, n)
                matrix[x][y][2] += a
            if matrix[x + 1][y][0] == matrix[x][y][0] and matrix[x + 1][y][1] == 0:
                r1, r2, a, matrix, d = calculate_connectivity(matrix, x + 1, y, n)
                matrix[x][y][2] += a
        else:
            # top-row
            if matrix[x][y + 1][0] == matrix[x][y][0] and matrix[x][y + 1][1] == 0:
                r1, r2, a, matrix, d = calculate_connectivity(matrix, x, y + 1, n)
                matrix[x][y][2] += a
            if matrix[x][y - 1][0] == matrix[x][y][0] and matrix[x][y - 1][1] == 0:
                r1, r2, a, matrix, d = calculate_connectivity(matrix, x, y - 1, n)
                matrix[x][y][2] += a
            if matrix[x + 1][y][0] == matrix[x][y][0] and matrix[x + 1][y][1] == 0:
                r1, r2, a, matrix, d = calculate_connectivity(matrix, x + 1, y, n)
                matrix[x][y][2] += a
    elif x == n - 1:
        if y == 0:
            # bottom-left
            if matrix[x][y + 1][0] == matrix[x][y][0] and matrix[x][y + 1][1] == 0:
                r1, r2, a, matrix, d = calculate_connectivity(matrix, x, y + 1, n)
                matrix[x][y][2] += a
            if matrix[x - 1][y][0] == matrix[x][y][0] and matrix[x - 1][y][1] == 0:
                r1, r2, a, matrix, d = calculate_connectivity(matrix, x - 1, y, n)
                matrix[x][y][2] += a
        elif y == n - 1:
            # bottom-right
            if matrix[x][y - 1][0] == matrix[x][y][0] and matrix[x][y - 1][1] == 0:
                r1, r2, a, matrix, d = calculate_connectivity(matrix, x, y - 1, n)
                matrix[x][y][2] += a
            if matrix[x - 1][y][0] == matrix[x][y][0] and matrix[x - 1][y][1] == 0:
                r1, r2, a, matrix, d = calculate_connectivity(matrix, x - 1, y, n)
                matrix[x][y][2] += a
        else:
            # bottom-row
            if matrix[x][y + 1][0] == matrix[x][y][0] and matrix[x][y + 1][1] == 0:
                r1, r2, a, matrix, d = calculate_connectivity(matrix, x, y + 1, n)
                matrix[x][y][2] += a
            if matrix[x][y - 1][0] == matrix[x][y][0] and matrix[x][y - 1][1] == 0:
                r1, r2, a, matrix, d = calculate_connectivity(matrix, x, y - 1, n)
                matrix[x][y][2] += a
            if matrix[x - 1][y][0] == matrix[x][y][0] and matrix[x - 1][y][1] == 0:
                r1, r2, a, matrix, d = calculate_connectivity(matrix, x - 1, y, n)
                matrix[x][y][2] += a
    else:
        if y == 0:
            # middle-left
            if matrix[x][y + 1][0] == matrix[x][y][0] and matrix[x][y + 1][1] == 0:
                r1, r2, a, matrix, d = calculate_connectivity(matrix, x, y + 1, n)
                matrix[x][y][2] += a
            if matrix[x - 1][y][0] == matrix[x][y][0] and matrix[x - 1][y][1] == 0:
                r1, r2, a, matrix, d = calculate_connectivity(matrix, x - 1, y, n)
                matrix[x][y][2] += a
            if matrix[x + 1][y][0] == matrix[x][y][0] and matrix[x + 1][y][1] == 0:
                r1, r2, a, matrix, d = calculate_connectivity(matrix, x + 1, y, n)
                matrix[x][y][2] += a
        elif y == n - 1:
            # middle-right
            if matrix[x][y - 1][0] == matrix[x][y][0] and matrix[x][y - 1][1] == 0:
                r1, r2, a, matrix, d = calculate_connectivity(matrix, x, y - 1, n)
                matrix[x][y][2] += a
            if matrix[x - 1][y][0] == matrix[x][y][0] and matrix[x - 1][y][1] == 0:
                r1, r2, a, matrix, d = calculate_connectivity(matrix, x - 1, y, n)
                matrix[x][y][2] += a
            if matrix[x + 1][y][0] == matrix[x][y][0] and matrix[x + 1][y][1] == 0:
                r1, r2, a, matrix, d = calculate_connectivity(matrix, x + 1, y, n)
                matrix[x][y][2] += a
        else:
            # middle-middle :-p
            if matrix[x][y - 1][0] == matrix[x][y][0] and matrix[x][y - 1][1] == 0:
                r1, r2, a, matrix, d = calculate_connectivity(matrix, x, y - 1, n)
                matrix[x][y][2] += a
            if matrix[x][y + 1][0] == matrix[x][y][0] and matrix[x][y + 1][1] == 0:
                r1, r2, a, matrix, d = calculate_connectivity(matrix, x, y + 1, n)
                matrix[x][y][2] += a
            if matrix[x - 1][y][0] == matrix[x][y][0] and matrix[x - 1][y][1] == 0:
                r1, r2, a, matrix, d = calculate_connectivity(matrix, x - 1, y, n)
                matrix[x][y][2] += a
            if matrix[x + 1][y][0] == matrix[x][y][0] and matrix[x + 1][y][1] == 0:
                r1, r2, a, matrix, d = calculate_connectivity(matrix, x + 1, y, n)
                matrix[x][y][2] += a

    return x, y, matrix[x][y][2], deepcopy(matrix), matrix[x][y][0]


def remove_fruits(matrix, x, y, n):
    # matrix = [cellvalue, visited, sumvalue]
    # return x-coord, y-coord, sumvalue, matrix
    matrix_copy_in_func = deepcopy(matrix)
    found = 0
    if x == y == 0 and n == 1:
        matrix_copy_in_func[x][y][0] = '*'
        return deepcopy(matrix_copy_in_func)
    matrix_copy_in_func[x][y][1] = 2
    if x == 0:
        if y == 0:
            # top-left
            if matrix_copy_in_func[x][y + 1][0] == matrix_copy_in_func[x][y][0] and matrix_copy_in_func[x][y + 1][
                1] == 1:
                matrix_copy_in_func = remove_fruits(matrix_copy_in_func, x, y + 1, n)
                found = 1
            if matrix_copy_in_func[x + 1][y][0] == matrix_copy_in_func[x][y][0] and matrix_copy_in_func[x + 1][y][
                1] == 1:
                matrix_copy_in_func = remove_fruits(matrix_copy_in_func, x + 1, y, n)
                found = 1
        elif y == n - 1:
            # top-right
            if matrix_copy_in_func[x][y - 1][0] == matrix_copy_in_func[x][y][0] and matrix_copy_in_func[x][y - 1][
                1] == 1:
                matrix_copy_in_func = remove_fruits(matrix_copy_in_func, x, y - 1, n)
                found = 1
            if matrix_copy_in_func[x + 1][y][0] == matrix_copy_in_func[x][y][0] and matrix_copy_in_func[x + 1][y][
                1] == 1:
                matrix_copy_in_func = remove_fruits(matrix_copy_in_func, x + 1, y, n)
                found = 1
        else:
            # top-row
            if matrix_copy_in_func[x][y + 1][0] == matrix_copy_in_func[x][y][0] and matrix_copy_in_func[x][y + 1][
                1] == 1:
                matrix_copy_in_func = remove_fruits(matrix_copy_in_func, x, y + 1, n)
                found = 1
            if matrix_copy_in_func[x][y - 1][0] == matrix_copy_in_func[x][y][0] and matrix_copy_in_func[x][y - 1][
                1] == 1:
                matrix_copy_in_func = remove_fruits(matrix_copy_in_func, x, y - 1, n)
                found = 1
            if matrix_copy_in_func[x + 1][y][0] == matrix_copy_in_func[x][y][0] and matrix_copy_in_func[x + 1][y][
                1] == 1:
                matrix_copy_in_func = remove_fruits(matrix_copy_in_func, x + 1, y, n)
                found = 1
    elif x == n - 1:
        if y == 0:
            # bottom-left
            if matrix_copy_in_func[x][y + 1][0] == matrix_copy_in_func[x][y][0] and matrix_copy_in_func[x][y + 1][
                1] == 1:
                matrix_copy_in_func = remove_fruits(matrix_copy_in_func, x, y + 1, n)
                found = 1
            if matrix_copy_in_func[x - 1][y][0] == matrix_copy_in_func[x][y][0] and matrix_copy_in_func[x - 1][y][
                1] == 1:
                matrix_copy_in_func = remove_fruits(matrix_copy_in_func, x - 1, y, n)
                found = 1
        elif y == n - 1:
            # bottom-right
            if matrix_copy_in_func[x][y - 1][0] == matrix_copy_in_func[x][y][0] and matrix_copy_in_func[x][y - 1][
                1] == 1:
                matrix_copy_in_func = remove_fruits(matrix_copy_in_func, x, y - 1, n)
                found = 1
            if matrix_copy_in_func[x - 1][y][0] == matrix_copy_in_func[x][y][0] and matrix_copy_in_func[x - 1][y][
                1] == 1:
                matrix_copy_in_func = remove_fruits(matrix_copy_in_func, x - 1, y, n)
                found = 1
        else:
            # bottom-row
            if matrix_copy_in_func[x][y + 1][0] == matrix_copy_in_func[x][y][0] and matrix_copy_in_func[x][y + 1][
                1] == 1:
                matrix_copy_in_func = remove_fruits(matrix_copy_in_func, x, y + 1, n)
                found = 1
            if matrix_copy_in_func[x][y - 1][0] == matrix_copy_in_func[x][y][0] and matrix_copy_in_func[x][y - 1][
                1] == 1:
                matrix_copy_in_func = remove_fruits(matrix_copy_in_func, x, y - 1, n)
                found = 1
            if matrix_copy_in_func[x - 1][y][0] == matrix_copy_in_func[x][y][0] and matrix_copy_in_func[x - 1][y][
                1] == 1:
                matrix_copy_in_func = remove_fruits(matrix_copy_in_func, x - 1, y, n)
                found = 1
    else:
        if y == 0:
            # middle-left
            if matrix_copy_in_func[x][y + 1][0] == matrix_copy_in_func[x][y][0] and matrix_copy_in_func[x][y + 1][
                1] == 1:
                matrix_copy_in_func = remove_fruits(matrix_copy_in_func, x, y + 1, n)
                found = 1
            if matrix_copy_in_func[x - 1][y][0] == matrix_copy_in_func[x][y][0] and matrix_copy_in_func[x - 1][y][
                1] == 1:
                matrix_copy_in_func = remove_fruits(matrix_copy_in_func, x - 1, y, n)
                found = 1
            if matrix_copy_in_func[x + 1][y][0] == matrix_copy_in_func[x][y][0] and matrix_copy_in_func[x + 1][y][
                1] == 1:
                matrix_copy_in_func = remove_fruits(matrix_copy_in_func, x + 1, y, n)
                found = 1
        elif y == n - 1:
            # middle-right
            if matrix_copy_in_func[x][y - 1][0] == matrix_copy_in_func[x][y][0] and matrix_copy_in_func[x][y - 1][
                1] == 1:
                matrix_copy_in_func = remove_fruits(matrix_copy_in_func, x, y - 1, n)
                found = 1
            if matrix_copy_in_func[x - 1][y][0] == matrix_copy_in_func[x][y][0] and matrix_copy_in_func[x - 1][y][
                1] == 1:
                matrix_copy_in_func = remove_fruits(matrix_copy_in_func, x - 1, y, n)
                found = 1
            if matrix_copy_in_func[x + 1][y][0] == matrix_copy_in_func[x][y][0] and matrix_copy_in_func[x + 1][y][
                1] == 1:
                matrix_copy_in_func = remove_fruits(matrix_copy_in_func, x + 1, y, n)
                found = 1
        else:
            # middle-middle :-p
            if matrix_copy_in_func[x][y - 1][0] == matrix_copy_in_func[x][y][0] and matrix_copy_in_func[x][y - 1][
                1] == 1:
                matrix_copy_in_func = remove_fruits(matrix_copy_in_func, x, y - 1, n)
                found = 1
            if matrix_copy_in_func[x][y + 1][0] == matrix_copy_in_func[x][y][0] and matrix_copy_in_func[x][y + 1][
                1] == 1:
                matrix_copy_in_func = remove_fruits(matrix_copy_in_func, x, y + 1, n)
                found = 1
            if matrix_copy_in_func[x - 1][y][0] == matrix_copy_in_func[x][y][0] and matrix_copy_in_func[x - 1][y][
                1] == 1:
                matrix_copy_in_func = remove_fruits(matrix_copy_in_func, x - 1, y, n)
                found = 1
            if matrix_copy_in_func[x + 1][y][0] == matrix_copy_in_func[x][y][0] and matrix_copy_in_func[x + 1][y][
                1] == 1:
                matrix_copy_in_func = remove_fruits(matrix_copy_in_func, x + 1, y, n)
                found = 1

    if found == 1:
        matrix_copy_in_func[x][y][0] = '*'
        return deepcopy(matrix_copy_in_func)
    else:
        matrix_copy_in_func[x][y][0] = '*'
        return deepcopy(matrix_copy_in_func)


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
            count = 0
            while count < c['*']:
                x = 0
                for x in range(n):
                    if row[x][0] == '*':
                        break
                aa = row.pop(x)
                row.append(aa)
                count += 1
            row.reverse()
    matrix1 = rotate(matrix1, 90)
    return deepcopy(matrix1)


def dict_fruit_has_fruit(dict_fruit_1):
    for x in dict_fruit_1:
        if dict_fruit_1[x][1] != -1:  # from the initialisation
            return True
    return False


def unset_visited(matrix):
    for x in matrix:
        for y in x:
            y[1] = 0
    return deepcopy(matrix)


def reset_visited(matrix):
    for x in matrix:
        for y in x:
            y[1] = 1
    return deepcopy(matrix)


def refine_selection(dict_fruit1, n):
    dict_fruit = deepcopy(dict_fruit1)
    l = len(dict_fruit)
    x = 0
    while x < len(dict_fruit)-1:
        if dict_fruit[x][0] == dict_fruit[x + 1][0] and dict_fruit[x][0] != 1 and dict_fruit[x][0] != 2:
            del dict_fruit[x + 1]
        else:
            x += 1
    l = len(dict_fruit)
    dict_fruit = dict_fruit[:(math.floor(l/2))]
    return deepcopy(dict_fruit)



def mark_conflicts(n, row, col, dict_fruit):
    for x in range(col, -1, -1):  # leftside
        if tuple([row, x]) in dict_fruit and tuple([row, col]) in dict_fruit and dict_fruit[tuple([row, x])][3] != \
                dict_fruit[tuple([row, col])][3]:
            break
        if tuple([row, x]) in dict_fruit and tuple([row, col]) in dict_fruit and dict_fruit[tuple([row, x])][0] == \
                dict_fruit[tuple([row, col])][0] and x != col and dict_fruit[tuple([row, x])][3] == \
                dict_fruit[tuple([row, col])][3]:
            del dict_fruit[tuple([row, x])]

    for x in range(col, n):  # rightside
        if tuple([row, x]) in dict_fruit and tuple([row, col]) in dict_fruit and dict_fruit[tuple([row, x])][3] != \
                dict_fruit[tuple([row, col])][3]:
            break
        if tuple([row, x]) in dict_fruit and tuple([row, col]) in dict_fruit and dict_fruit[tuple([row, x])][0] == \
                dict_fruit[tuple([row, col])][0] and x != col and dict_fruit[tuple([row, x])][3] == \
                dict_fruit[tuple([row, col])][3]:
            del dict_fruit[tuple([row, x])]

    for x in range(row, -1, -1):  # top
        if tuple([x, col]) in dict_fruit and tuple([row, col]) in dict_fruit and dict_fruit[tuple([x, col])][3] != \
                dict_fruit[tuple([row, col])][3]:
            break
        if tuple([x, col]) in dict_fruit and tuple([row, col]) in dict_fruit and dict_fruit[tuple([x, col])][0] == \
                dict_fruit[tuple([row, col])][0] and x != row and dict_fruit[tuple([x, col])][3] == \
                dict_fruit[tuple([row, col])][3]:
            del dict_fruit[tuple([x, col])]

    for x in range(row, n):  # bottom
        if tuple([x, col]) in dict_fruit and tuple([row, col]) in dict_fruit and dict_fruit[tuple([x, col])][3] != \
                dict_fruit[tuple([row, col])][3]:
            break
        if tuple([x, col]) in dict_fruit and tuple([row, col]) in dict_fruit and dict_fruit[tuple([x, col])][0] == \
                dict_fruit[tuple([row, col])][0] and x != row and dict_fruit[tuple([x, col])][3] == \
                dict_fruit[tuple([row, col])][3]:
            del dict_fruit[tuple([x, col])]

        return deepcopy(dict_fruit)


def my_game(n, matrix, alpha, beta, ismaxplayer, myvalue, oppvalue, depth, firstmove, time):
    # matrix = [cellvalue, visited, sumvalue]
    # dictfruit = {0 : [max_value, x-coord, y-coord]}

    # returns number_of_elements_removed, matrix_after_removal, x_coord, y_coord

    dict_fruit = deque([])
    empty = deepcopy(matrix)
    for x in range(n):
        for y in range(n):
            if matrix[x][y][0] != '*':
                matrix = deepcopy(empty)
                x1, y1, z, matrixdummy, v = calculate_connectivity(matrix, x, y, n)
                temp = [0, -1, -1, 0]
                temp[0] = z  # number of cells
                temp[1] = x1  # x coordinate
                temp[2] = y1  # y coordinate
                temp[3] = v  # fruit type
                dict_fruit.append(temp)
    dict_fruit = deque(reversed(sorted(dict_fruit, key=lambda h: h[0])))

    if len(dict_fruit) == 0 or depth == 1:
        return myvalue - oppvalue
    dict_fruit = refine_selection(dict_fruit, n)
    dict_fruit = deque(reversed(sorted(dict_fruit, key=lambda h: h[0])))
    if ismaxplayer:
        # for x in dict_fruit.items():
        #     print(x)
        bestvalue = -maxsize
        matret = []
        # refining still to be dealt with
        while len(dict_fruit) > 0:
            # fruit_to_remove = [x]
            fruit_to_remove = dict_fruit.popleft()
            myvalue += fruit_to_remove[0] ** 2
            matrix1 = remove_fruits(matrix, fruit_to_remove[1], fruit_to_remove[2], n)
            matrix1 = apply_gravity(matrix1)
            # print_matrix(matrix1)
            # print(fruit_to_remove)
            # print(depth)
            # print()
            if firstmove:
                matret = deepcopy(matrix1)
            value = my_game(n, matrix1, alpha, beta, False, myvalue, oppvalue, depth + 1, False, t)
            bestvalue = max(bestvalue, value)
            alpha = max(alpha, bestvalue)
            if beta <= alpha:
                break
        if firstmove:
            return matret, bestvalue
        return bestvalue
    else:
        bestvalue = maxsize
        matret = []
        # refining still to be dealt with
        while len(dict_fruit) > 0:
            # fruit_to_remove = [x]
            fruit_to_remove = dict_fruit.popleft()
            oppvalue += fruit_to_remove[0] ** 2
            matrix1 = remove_fruits(matrix, fruit_to_remove[1], fruit_to_remove[2], n)
            matrix1 = apply_gravity(matrix1)
            # print_matrix(matrix1)
            # print(fruit_to_remove)
            # print(depth)
            # print()
            if firstmove:
                matret = deepcopy(matrix1)
            value = my_game(n, matrix1, alpha, beta, True, myvalue, oppvalue, depth + 1, False, t)
            bestvalue = min(bestvalue, value)
            beta = min(beta, bestvalue)
            if beta <= alpha:
                break
        if firstmove:
            return matret, bestvalue
        return bestvalue


if __name__ == "__main__":
    # matrix = [cellvalue, visited, sumvalue]
    # dictfruit = {0 : [max_value, x-coord, y-coord]}

    f = open("input.txt", "r")
    n = int(f.readline().strip())
    p = int(f.readline().strip())
    t = float(f.readline().strip())

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
    print_matrix(empty)
    matrix, value = my_game(n, empty, -maxsize, maxsize, True, 0, 0, 0, True, t)
    # print_matrix(matrix)
    output = open("output.txt", "w")
    print_output(matrix, output)
    output.close()
