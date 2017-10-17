# from __future__ import print_function
from collections import Counter, deque
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


def print_matrix_only_value(matrix):
    for eachrow in matrix:
        for eachcolumn in eachrow:
            print(eachcolumn[0], end='')
        print()


def calculate_connectivity(matrix, x, y, n):
    # matrix = [cellvalue, visited, sumvalue]
    # return x-coord, y-coord, sumvalue, matrix,
    if x == y == 0 and n == 1:
        return x, y, matrix[x][y][2], deepcopy(matrix)  # , matrix[x][y][0]
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

    return x, y, matrix[x][y][2], deepcopy(matrix)  # , matrix[x][y][0]



def send_group_count_to_all(matrix, x, y, n, cellcount):
    # matrix, cellcount =  [cellvalue, visited, sumvalue]
    # return x-coord, y-coord, sumvalue, matrix,
    if x == y == 0 and n == 1:
        return deepcopy(matrix)  # , matrix[x][y][0]
    matrix[x][y][1] = 1
    if x == 0:
        if y == 0:
            # top-left
            if matrix[x][y + 1][0] == matrix[x][y][0] and matrix[x][y + 1][1] == 0:
                matrix = send_group_count_to_all(matrix, x, y + 1, n, cellcount)
            if matrix[x + 1][y][0] == matrix[x][y][0] and matrix[x + 1][y][1] == 0:
                matrix = send_group_count_to_all(matrix, x + 1, y, n, cellcount)
        elif y == n - 1:
            # top-right
            if matrix[x][y - 1][0] == matrix[x][y][0] and matrix[x][y - 1][1] == 0:
                matrix = send_group_count_to_all(matrix, x, y - 1, n, cellcount)
            if matrix[x + 1][y][0] == matrix[x][y][0] and matrix[x + 1][y][1] == 0:
                matrix = send_group_count_to_all(matrix, x + 1, y, n, cellcount)
        else:
            # top-row
            if matrix[x][y + 1][0] == matrix[x][y][0] and matrix[x][y + 1][1] == 0:
                matrix = send_group_count_to_all(matrix, x, y + 1, n, cellcount)
            if matrix[x][y - 1][0] == matrix[x][y][0] and matrix[x][y - 1][1] == 0:
                matrix = send_group_count_to_all(matrix, x, y - 1, n, cellcount)
            if matrix[x + 1][y][0] == matrix[x][y][0] and matrix[x + 1][y][1] == 0:
                matrix = send_group_count_to_all(matrix, x + 1, y, n, cellcount)
    elif x == n - 1:
        if y == 0:
            # bottom-left
            if matrix[x][y + 1][0] == matrix[x][y][0] and matrix[x][y + 1][1] == 0:
                matrix = send_group_count_to_all(matrix, x, y + 1, n, cellcount)
            if matrix[x - 1][y][0] == matrix[x][y][0] and matrix[x - 1][y][1] == 0:
                matrix = send_group_count_to_all(matrix, x - 1, y, n, cellcount)
        elif y == n - 1:
            # bottom-right
            if matrix[x][y - 1][0] == matrix[x][y][0] and matrix[x][y - 1][1] == 0:
                matrix = send_group_count_to_all(matrix, x, y - 1, n, cellcount)
            if matrix[x - 1][y][0] == matrix[x][y][0] and matrix[x - 1][y][1] == 0:
                matrix = send_group_count_to_all(matrix, x - 1, y, n, cellcount)
        else:
            # bottom-row
            if matrix[x][y + 1][0] == matrix[x][y][0] and matrix[x][y + 1][1] == 0:
                matrix = send_group_count_to_all(matrix, x, y + 1, n, cellcount)
            if matrix[x][y - 1][0] == matrix[x][y][0] and matrix[x][y - 1][1] == 0:
                matrix = send_group_count_to_all(matrix, x, y - 1, n, cellcount)
            if matrix[x - 1][y][0] == matrix[x][y][0] and matrix[x - 1][y][1] == 0:
                matrix = send_group_count_to_all(matrix, x - 1, y, n, cellcount)
    else:
        if y == 0:
            # middle-left
            if matrix[x][y + 1][0] == matrix[x][y][0] and matrix[x][y + 1][1] == 0:
                matrix = send_group_count_to_all(matrix, x, y + 1, n, cellcount)
            if matrix[x - 1][y][0] == matrix[x][y][0] and matrix[x - 1][y][1] == 0:
                matrix = send_group_count_to_all(matrix, x - 1, y, n, cellcount)
            if matrix[x + 1][y][0] == matrix[x][y][0] and matrix[x + 1][y][1] == 0:
                matrix = send_group_count_to_all(matrix, x + 1, y, n, cellcount)
        elif y == n - 1:
            # middle-right
            if matrix[x][y - 1][0] == matrix[x][y][0] and matrix[x][y - 1][1] == 0:
                matrix = send_group_count_to_all(matrix, x, y - 1, n, cellcount)
            if matrix[x - 1][y][0] == matrix[x][y][0] and matrix[x - 1][y][1] == 0:
                matrix = send_group_count_to_all(matrix, x - 1, y, n, cellcount)
            if matrix[x + 1][y][0] == matrix[x][y][0] and matrix[x + 1][y][1] == 0:
                matrix = send_group_count_to_all(matrix, x + 1, y, n, cellcount)
        else:
            # middle-middle :-p
            if matrix[x][y - 1][0] == matrix[x][y][0] and matrix[x][y - 1][1] == 0:
                matrix = send_group_count_to_all(matrix, x, y - 1, n, cellcount)
            if matrix[x][y + 1][0] == matrix[x][y][0] and matrix[x][y + 1][1] == 0:
                matrix = send_group_count_to_all(matrix, x, y + 1, n, cellcount)
            if matrix[x - 1][y][0] == matrix[x][y][0] and matrix[x - 1][y][1] == 0:
                matrix = send_group_count_to_all(matrix, x - 1, y, n, cellcount)
            if matrix[x + 1][y][0] == matrix[x][y][0] and matrix[x + 1][y][1] == 0:
                matrix = send_group_count_to_all(matrix, x + 1, y, n, cellcount)
    matrix[x][y][0] = cellcount
    return deepcopy(matrix)


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
                1] <= 1:
                matrix_copy_in_func = remove_fruits(matrix_copy_in_func, x, y + 1, n)
                found = 1
            if matrix_copy_in_func[x + 1][y][0] == matrix_copy_in_func[x][y][0] and matrix_copy_in_func[x + 1][y][
                1] <= 1:
                matrix_copy_in_func = remove_fruits(matrix_copy_in_func, x + 1, y, n)
                found = 1
        elif y == n - 1:
            # top-right
            if matrix_copy_in_func[x][y - 1][0] == matrix_copy_in_func[x][y][0] and matrix_copy_in_func[x][y - 1][
                1] <= 1:
                matrix_copy_in_func = remove_fruits(matrix_copy_in_func, x, y - 1, n)
                found = 1
            if matrix_copy_in_func[x + 1][y][0] == matrix_copy_in_func[x][y][0] and matrix_copy_in_func[x + 1][y][
                1] <= 1:
                matrix_copy_in_func = remove_fruits(matrix_copy_in_func, x + 1, y, n)
                found = 1
        else:
            # top-row
            if matrix_copy_in_func[x][y + 1][0] == matrix_copy_in_func[x][y][0] and matrix_copy_in_func[x][y + 1][
                1] <= 1:
                matrix_copy_in_func = remove_fruits(matrix_copy_in_func, x, y + 1, n)
                found = 1
            if matrix_copy_in_func[x][y - 1][0] == matrix_copy_in_func[x][y][0] and matrix_copy_in_func[x][y - 1][
                1] <= 1:
                matrix_copy_in_func = remove_fruits(matrix_copy_in_func, x, y - 1, n)
                found = 1
            if matrix_copy_in_func[x + 1][y][0] == matrix_copy_in_func[x][y][0] and matrix_copy_in_func[x + 1][y][
                1] <= 1:
                matrix_copy_in_func = remove_fruits(matrix_copy_in_func, x + 1, y, n)
                found = 1
    elif x == n - 1:
        if y == 0:
            # bottom-left
            if matrix_copy_in_func[x][y + 1][0] == matrix_copy_in_func[x][y][0] and matrix_copy_in_func[x][y + 1][
                1] <= 1:
                matrix_copy_in_func = remove_fruits(matrix_copy_in_func, x, y + 1, n)
                found = 1
            if matrix_copy_in_func[x - 1][y][0] == matrix_copy_in_func[x][y][0] and matrix_copy_in_func[x - 1][y][
                1] <= 1:
                matrix_copy_in_func = remove_fruits(matrix_copy_in_func, x - 1, y, n)
                found = 1
        elif y == n - 1:
            # bottom-right
            if matrix_copy_in_func[x][y - 1][0] == matrix_copy_in_func[x][y][0] and matrix_copy_in_func[x][y - 1][
                1] <= 1:
                matrix_copy_in_func = remove_fruits(matrix_copy_in_func, x, y - 1, n)
                found = 1
            if matrix_copy_in_func[x - 1][y][0] == matrix_copy_in_func[x][y][0] and matrix_copy_in_func[x - 1][y][
                1] <= 1:
                matrix_copy_in_func = remove_fruits(matrix_copy_in_func, x - 1, y, n)
                found = 1
        else:
            # bottom-row
            if matrix_copy_in_func[x][y + 1][0] == matrix_copy_in_func[x][y][0] and matrix_copy_in_func[x][y + 1][
                1] <= 1:
                matrix_copy_in_func = remove_fruits(matrix_copy_in_func, x, y + 1, n)
                found = 1
            if matrix_copy_in_func[x][y - 1][0] == matrix_copy_in_func[x][y][0] and matrix_copy_in_func[x][y - 1][
                1] <= 1:
                matrix_copy_in_func = remove_fruits(matrix_copy_in_func, x, y - 1, n)
                found = 1
            if matrix_copy_in_func[x - 1][y][0] == matrix_copy_in_func[x][y][0] and matrix_copy_in_func[x - 1][y][
                1] <= 1:
                matrix_copy_in_func = remove_fruits(matrix_copy_in_func, x - 1, y, n)
                found = 1
    else:
        if y == 0:
            # middle-left
            if matrix_copy_in_func[x][y + 1][0] == matrix_copy_in_func[x][y][0] and matrix_copy_in_func[x][y + 1][
                1] <= 1:
                matrix_copy_in_func = remove_fruits(matrix_copy_in_func, x, y + 1, n)
                found = 1
            if matrix_copy_in_func[x - 1][y][0] == matrix_copy_in_func[x][y][0] and matrix_copy_in_func[x - 1][y][
                1] <= 1:
                matrix_copy_in_func = remove_fruits(matrix_copy_in_func, x - 1, y, n)
                found = 1
            if matrix_copy_in_func[x + 1][y][0] == matrix_copy_in_func[x][y][0] and matrix_copy_in_func[x + 1][y][
                1] <= 1:
                matrix_copy_in_func = remove_fruits(matrix_copy_in_func, x + 1, y, n)
                found = 1
        elif y == n - 1:
            # middle-right
            if matrix_copy_in_func[x][y - 1][0] == matrix_copy_in_func[x][y][0] and matrix_copy_in_func[x][y - 1][
                1] <= 1:
                matrix_copy_in_func = remove_fruits(matrix_copy_in_func, x, y - 1, n)
                found = 1
            if matrix_copy_in_func[x - 1][y][0] == matrix_copy_in_func[x][y][0] and matrix_copy_in_func[x - 1][y][
                1] <= 1:
                matrix_copy_in_func = remove_fruits(matrix_copy_in_func, x - 1, y, n)
                found = 1
            if matrix_copy_in_func[x + 1][y][0] == matrix_copy_in_func[x][y][0] and matrix_copy_in_func[x + 1][y][
                1] <= 1:
                matrix_copy_in_func = remove_fruits(matrix_copy_in_func, x + 1, y, n)
                found = 1
        else:
            # middle-middle :-p
            if matrix_copy_in_func[x][y - 1][0] == matrix_copy_in_func[x][y][0] and matrix_copy_in_func[x][y - 1][
                1] <= 1:
                matrix_copy_in_func = remove_fruits(matrix_copy_in_func, x, y - 1, n)
                found = 1
            if matrix_copy_in_func[x][y + 1][0] == matrix_copy_in_func[x][y][0] and matrix_copy_in_func[x][y + 1][
                1] <= 1:
                matrix_copy_in_func = remove_fruits(matrix_copy_in_func, x, y + 1, n)
                found = 1
            if matrix_copy_in_func[x - 1][y][0] == matrix_copy_in_func[x][y][0] and matrix_copy_in_func[x - 1][y][
                1] <= 1:
                matrix_copy_in_func = remove_fruits(matrix_copy_in_func, x - 1, y, n)
                found = 1
            if matrix_copy_in_func[x + 1][y][0] == matrix_copy_in_func[x][y][0] and matrix_copy_in_func[x + 1][y][
                1] <= 1:
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
    x = 0
    while x < len(dict_fruit) - 1:
        if dict_fruit[x][0] == dict_fruit[x + 1][0] and dict_fruit[x][0] != 1 and dict_fruit[x][0] != 2:
            del dict_fruit[x + 1]
        else:
            x += 1
    l = len(dict_fruit)
    if l <= 2 * n:
        pass
    elif l <= 25:
        dict_fruit = [dict_fruit[x] for x in range(int(math.floor(l / 2)))]
    elif l <= 40:
        dict_fruit = [dict_fruit[x] for x in range(int(math.floor(l / 3)))]
    elif l <= 70:
        dict_fruit = [dict_fruit[x] for x in range(int(math.floor(l / 4)))]
    else:
        dict_fruit = [dict_fruit[x] for x in range(int(math.floor(l / 5)))]
    return deepcopy(dict_fruit)


def my_game(n, matrix, alpha, beta, is_max_player, my_value, opp_value, depth, first_move, time_spent, deadline_time):
    # matrix = [cellvalue, visited, sumvalue]
    # dictfruit = {0 : [max_value, x-coord, y-coord]}

    # returns number_of_elements_removed, matrix_after_removal, x_coord, y_coord
    at_start_game = time()
    dict_fruit = deque([])
    empty = deepcopy(matrix)
    # y - AB; x - 123
    # connectivity check
    for x in range(n):
        for y in range(n):
            if matrix[x][y][0] != '*':
                # matrix = unset_visited(matrix)
                matrix = unset_visited(empty)
                x1, y1, z, matrix_dummy = calculate_connectivity(matrix, x, y, n)
                # z = calculate_connectivity(matrix, x, y, n)
                matrix = unset_visited(matrix)
                matrix = send_group_count_to_all(matrix, x, y, n, '*')
                dict_fruit.append([z, x1, y1, deepcopy(matrix)])  # number of cells,  x coordinate, y coordinate
                # if deadline_time - time_spent <= 5 or n >= 15:
                #     if first_move:
                #         return dict_fruit[-1][3], dict_fruit[-1][0]**2, x, y
                #     else:
                #         return my_value - opp_value
                # print()
                # print_matrix_only_value(matrix)
                # print()
    matrix = deepcopy(empty)
    dict_fruit = deque(reversed(sorted(dict_fruit, key=lambda h: h[0])))
    if len(dict_fruit)>0:
        temp_mat = apply_gravity(dict_fruit[0][3])
    else:
        temp_mat = deepcopy(matrix)
    # max_depth = 1 if time <= 5 else 2
    before_check = time()
    time2 = time()
    time_spent += before_check - at_start_game
    if deadline_time - time_spent <= 5 or n >= 15:
        if first_move:
            return temp_mat, my_value - opp_value, dict_fruit[0][1], dict_fruit[0][2]
        else:
            return my_value - opp_value
    if len(dict_fruit) == 0 or depth == 3:
        return my_value - opp_value
    mat_ret = []
    x_used = y_used = 0
    if is_max_player:
        best_value = -maxsize
        x_used = y_used = 0
        while len(dict_fruit) > 0:
            fruit_to_remove = dict_fruit.popleft()
            my_value += fruit_to_remove[0] ** 2
            matrix1 = apply_gravity(remove_fruits(matrix, fruit_to_remove[1], fruit_to_remove[2], n))
            time3 = time()
            time_spent += time3 - time2
            value = my_game(n, matrix1, alpha, beta, False, my_value, opp_value, depth + 1, False, time_spent, t)
            if first_move:
                if best_value < value:
                    best_value = value
                    mat_ret, x_used, y_used = deepcopy(matrix1), fruit_to_remove[1], fruit_to_remove[2]
            else:
                best_value = max(best_value, value)
            alpha = max(alpha, best_value)
            if beta <= alpha:
                break
    else:
        best_value = maxsize
        while len(dict_fruit) > 0:
            fruit_to_remove = dict_fruit.popleft()
            opp_value += fruit_to_remove[0] ** 2
            matrix1 = apply_gravity(remove_fruits(matrix, fruit_to_remove[1], fruit_to_remove[2], n))
            time3 = time()
            time_spent += time3 - time2
            value = my_game(n, matrix1, alpha, beta, True, my_value, opp_value, depth + 1, False, time_spent, t)
            best_value = min(best_value, value)
            beta = min(beta, best_value)
            if beta <= alpha:
                break
    if first_move:
        return mat_ret, best_value, x_used, y_used
    return best_value


if __name__ == "__main__":
    # matrix = [cellvalue, visited, sumvalue]
    # dictfruit = {0 : [max_value, x-coord, y-coord]}

    f = open("input.txt", "r")
    n = int(f.readline().strip())
    p = int(f.readline().strip())
    t = float(f.readline().strip())
    # print(n)
    # print(p)
    # print(t)
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
    # print_matrix_only_value(empty)
    start = time()
    before_game = time()
    matrix, value, xv, yv = my_game(n, empty, -maxsize, maxsize, True, 0, 0, 0, True, before_game - start, t)
    end = time()
    output = open("output.txt", "w")
    output.write(chr(ord('A') + yv))
    output.write(str(1 + xv))
    output.write("\n")
    print()
    # print_matrix_only_value(matrix)
    print(end - start)
    print(value)
    print_output(matrix, output)
    output.close()
