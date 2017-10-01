from collections import OrderedDict
import math
from copy import deepcopy


def print_matrix(matrix):
    for eachrow in matrix:
        for eachcolumn in eachrow:
            print("[ ", end='')
            for eachelement in eachcolumn:
                print(eachelement, end=' ')
            print("] ,", end='')
        print()


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
                matrix1 = remove_fruits(matrix, x, y + 1, n)
                found = 1
            if matrix[x + 1][y][0] == matrix[x][y][0] and matrix[x + 1][y][1] == 1:
                matrix1 = remove_fruits(matrix1, x + 1, y, n)
                found = 1
        elif y == n - 1:
            # top-right
            if matrix[x][y - 1][0] == matrix[x][y][0] and matrix[x][y - 1][1] == 1:
                matrix1 = remove_fruits(matrix, x, y - 1, n)
                found = 1
            if matrix[x + 1][y][0] == matrix[x][y][0] and matrix[x + 1][y][1] == 1:
                matrix1 = remove_fruits(matrix, x + 1, y, n)
                found = 1
        else:
            # top-row
            if matrix[x][y + 1][0] == matrix[x][y][0] and matrix[x][y + 1][1] == 1:
                matrix1 = remove_fruits(matrix, x, y + 1, n)
                found = 1
            if matrix[x][y - 1][0] == matrix[x][y][0] and matrix[x][y - 1][1] == 1:
                matrix1 = remove_fruits(matrix, x, y - 1, n)
                found = 1
            if matrix[x + 1][y][0] == matrix[x][y][0] and matrix[x + 1][y][1] == 1:
                matrix1 = remove_fruits(matrix, x + 1, y, n)
                found = 1
    elif x == n - 1:
        if y == 0:
            # bottom-left
            if matrix[x][y + 1][0] == matrix[x][y][0] and matrix[x][y + 1][1] == 1:
                matrix1 = remove_fruits(matrix, x, y + 1, n)
                # matrix1[x][0] = '*'
                found = 1
            if matrix[x - 1][y][0] == matrix[x][y][0] and matrix[x - 1][y][1] == 1:
                matrix1 = remove_fruits(matrix, x - 1, y, n)
                found = 1
        elif y == n - 1:
            # bottom-right
            if matrix[x][y - 1][0] == matrix[x][y][0] and matrix[x][y - 1][1] == 1:
                matrix1 = remove_fruits(matrix, x, y - 1, n)
                found = 1
            if matrix[x - 1][y][0] == matrix[x][y][0] and matrix[x - 1][y][1] == 1:
                matrix1 = remove_fruits(matrix, x - 1, y, n)
                found = 1
        else:
            # bottom-row
            if matrix[x][y + 1][0] == matrix[x][y][0] and matrix[x][y + 1][1] == 1:
                matrix1 = remove_fruits(matrix, x, y + 1, n)
                found = 1
            if matrix[x][y - 1][0] == matrix[x][y][0] and matrix[x][y - 1][1] == 1:
                matrix1 = remove_fruits(matrix, x, y - 1, n)
                found = 1
            if matrix[x - 1][y][0] == matrix[x][y][0] and matrix[x - 1][y][1] == 1:
                matrix1 = remove_fruits(matrix, x - 1, y, n)
                found = 1
    else:
        if y == 0:
            # middle-left
            if matrix[x][y + 1][0] == matrix[x][y][0] and matrix[x][y + 1][1] == 1:
                matrix1 = remove_fruits(matrix, x, y + 1, n)
                found = 1
            if matrix[x - 1][y][0] == matrix[x][y][0] and matrix[x - 1][y][1] == 1:
                matrix1 = remove_fruits(matrix, x - 1, y, n)
                found = 1
            if matrix[x + 1][y][0] == matrix[x][y][0] and matrix[x + 1][y][1] == 1:
                matrix1 = remove_fruits(matrix, x + 1, y, n)
                found = 1
        elif y == n - 1:
            # middle-right
            if matrix[x][y - 1][0] == matrix[x][y][0] and matrix[x][y - 1][1] == 1:
                matrix1 = remove_fruits(matrix, x, y - 1, n)
                found = 1
            if matrix[x - 1][y][0] == matrix[x][y][0] and matrix[x - 1][y][1] == 1:
                matrix1 = remove_fruits(matrix, x - 1, y, n)
                found = 1
            if matrix[x + 1][y][0] == matrix[x][y][0] and matrix[x + 1][y][1] == 1:
                matrix1 = remove_fruits(matrix, x + 1, y, n)
                found = 1
        else:
            # middle-middle :-p
            if matrix[x][y - 1][0] == matrix[x][y][0] and matrix[x][y - 1][1] == 1:
                matrix1 = remove_fruits(matrix, x, y - 1, n)
                found = 1
            if matrix[x][y + 1][0] == matrix[x][y][0] and matrix[x][y + 1][1] == 1:
                matrix1 = remove_fruits(matrix, x, y + 1, n)
                found = 1
            if matrix[x - 1][y][0] == matrix[x][y][0] and matrix[x - 1][y][1] == 1:
                matrix1 = remove_fruits(matrix, x - 1, y, n)
                found = 1
            if matrix[x + 1][y][0] == matrix[x][y][0] and matrix[x + 1][y][1] == 1:
                matrix1 = remove_fruits(matrix, x + 1, y, n)
                found = 1

    if found == 1:
        # print_matrix(matrix1)
        matrix1[x][y][0] = '*'
        return deepcopy(matrix1)
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


# def apply_gravity(matrix):
#     n = len(matrix)
#     matrix = rotate(matrix, 90)
#     for row in matrix:
#         star_found = 0
#         for x in row:
#             if star_found == 0 and type():




def my_game(n, matrix, dict_fruit, depth):
    # matrix = [cellvalue, visited, sumvalue]
    # dictfruit = {0 : [max_value, x-coord, y-coord]}

    if depth == 5:
        return 0  # ?  ?
    for x in range(n):
        for y in range(n):
            x1, y1, z, matrix1 = calculate_connectivity(matrix, x, y, n)
            if z > dict_fruit[matrix[x][y][0]][0]:
                dict_fruit[matrix[x][y][0]][0] = z
                dict_fruit[matrix[x][y][0]][1] = x1
                dict_fruit[matrix[x][y][0]][2] = y1
    # max_value = max([x[0] for x in dict_fruit.values()])
    print(dict_fruit)
    # print_matrix(matrix1)
    # choose fruit
    dict_fruit = OrderedDict(reversed(sorted(dict_fruit.items(), key=lambda h: h[1][0])))

    fruit_to_remove = dict_fruit.popitem(False)
    max_value = fruit_to_remove
    print(fruit_to_remove)

    # dictfruit = {0 : [max_value, x-coord, y-coord]}
    print_matrix(matrix)
    print()
    # remove those fruits - replace with *
    matrix = remove_fruits(matrix, fruit_to_remove[1][1], fruit_to_remove[1][2], n)

    print_matrix(matrix)
    # apply gravity
    # matrix = apply_gravity(matrix)

    # create 2 branches

    # choose the best of the result

    # return best value
    return max_value


if __name__ == "__main__":
    # matrix = [cellvalue, visited, sumvalue]
    f = open("input.txt", "r")
    n = int(f.readline().strip())
    p = int(f.readline().strip())
    t = float(f.readline().strip())
    # dictfruit = {0 : [max_value, x-coord, y-coord]}

    dict_fruit = {x: [0, -1, -1] for x in range(p)}
    dict_fruit = OrderedDict(dict_fruit)
    matrix = []
    for i in range(n):
        line = [[int(x), 0, 1] for x in f.readline().strip()]
        matrix.append(line)
    empty = deepcopy(matrix)

    # calculate the max number of fruits that can be picked
    print(my_game(n, empty, dict_fruit, 0))