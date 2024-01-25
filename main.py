import random

import matplotlib.pyplot as plt
import numpy as np


def generate_matrix(x):
    matrix = [[[random.randint(10, 50), 0, 1] for _ in range(x)] for _ in range(x)]
    return matrix


def compare_matrix(matrix):
    offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    numbers = [1, 2, 3, 4, 6, 7, 8, 9]
    size = len(matrix)
    for i in range(size):
        for j in range(size):
            current = matrix[i][j][0]
            lowest = current
            lowest_index = -1
            for k in range(8):
                x = i + offsets[k][0]
                y = j + offsets[k][1]
                if 0 <= x < size and 0 <= y < size:
                    neighbor = matrix[x][y][0]
                    if neighbor < current and neighbor < lowest:
                        lowest = neighbor
                        lowest_index = k
            if lowest_index != -1:
                matrix[i][j][1] = numbers[lowest_index]
            else:
                matrix[i][j][1] = 5
    return matrix


def modify_matrix(matrix, direction):
    offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    numbers = [1, 2, 3, 4, 6, 7, 8, 9]
    size = len(matrix)
    if direction == 1:
        for i in range(size):
            for j in range(size):
                current = matrix[i][j][2]
                position = matrix[i][j][1]
                if position == 0 or position == 5:
                    pass
                else:
                    index = numbers.index(position)
                    x = i + offsets[index][0]
                    y = j + offsets[index][1]
                    if 0 <= x < size and 0 <= y < size:
                        matrix[x][y][2] += current
    elif direction == 4:
        for i in range(size - 1, -1, -1):
            for j in range(size - 1, -1, -1):
                current = matrix[i][j][2]
                position = matrix[i][j][1]
                if position == 0 or position == 5:
                    pass
                else:
                    index = numbers.index(position)
                    x = i + offsets[index][0]
                    y = j + offsets[index][1]
                    if 0 <= x < size and 0 <= y < size:
                        matrix[x][y][2] += current
    elif direction == 3:
        for i in range(size - 1, -1, -1):
            for j in range(size):
                current = matrix[i][j][2]
                position = matrix[i][j][1]
                if position == 0 or position == 5:
                    pass
                else:
                    index = numbers.index(position)
                    x = i + offsets[index][0]
                    y = j + offsets[index][1]
                    if 0 <= x < size and 0 <= y < size:
                        matrix[x][y][2] += current
    elif direction == 2:
        for i in range(size):
            for j in range(size - 1, -1, -1):
                current = matrix[i][j][2]
                position = matrix[i][j][1]
                if position == 0 or position == 5:
                    pass
                else:
                    index = numbers.index(position)
                    x = i + offsets[index][0]
                    y = j + offsets[index][1]
                    if 0 <= x < size and 0 <= y < size:
                        matrix[x][y][2] += current
    else:
        print("Invalid direction")
    return matrix


matrix_size = 30
result_matrix = generate_matrix(matrix_size)
result_matrix = compare_matrix(result_matrix)
result_matrix = modify_matrix(result_matrix, 1)
result_matrix = modify_matrix(result_matrix, 4)
result_matrix = modify_matrix(result_matrix, 2)
result_matrix = modify_matrix(result_matrix, 3)
for row in result_matrix:
    print(row)
print('====================================================================================================================================================================================================================================================================================================================================')

third_value_matrix = [[pixel[2] for pixel in row] for row in result_matrix]
for row in third_value_matrix:
    for i in range(len(row)):
        if row[i] == 1:
            row[i] = 0
for row in third_value_matrix[::-1]:
    print(row)

colors = ["blue", "green", "yellow", "red"]
shades = [400, 1000]

avg = np.mean(third_value_matrix)

lower_mean = np.mean([x for x in np.ravel(third_value_matrix) if x < avg])

upper_mean = np.mean([x for x in np.ravel(third_value_matrix) if x > avg])

thresholds = [lower_mean, avg, upper_mean]


def get_color_and_shade(value):
    index = np.searchsorted(thresholds, value)
    color = colors[index]
    if index == 0:
        lower_limit = 0
    else:
        lower_limit = thresholds[index - 1]
    if index == len(colors) - 1:
        upper_limit = np.max(third_value_matrix)
    else:
        upper_limit = thresholds[index]
    ratio = (value - lower_limit) / (upper_limit - lower_limit)
    shade = shades[0] + ratio * (shades[1] - shades[0])
    return color, shade


color_matrix = []

for row in third_value_matrix:
    color_row = []
    for value in row:
        color, shade = get_color_and_shade(value)
        color_row.append((color, shade))
    color_matrix.append(color_row)

color_matrix = np.array(color_matrix)

fig, ax = plt.subplots()

for i in range(color_matrix.shape[0]):
    for j in range(color_matrix.shape[1]):
        color, shade = color_matrix[i, j]
        ax.add_patch(plt.Rectangle((j, i), 1, 1, color=color, alpha=(float(shade) / 1000)))

ax.set_xlim(0, color_matrix.shape[1])
ax.set_ylim(0, color_matrix.shape[0])
ax.set_aspect("equal")

ax.set_xticks([])
ax.set_yticks([])

plt.show()
