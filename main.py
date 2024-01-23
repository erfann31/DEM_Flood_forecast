import random

import matplotlib.pyplot as plt
import numpy as np


def generate_matrix(x):
    matrix = [[[random.randint(10, 50), 0, 1] for _ in range(x)] for _ in range(x)]
    return matrix


def compare_matrix(matrix):
    # Define the offsets for the eight neighbors
    offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    # Define the numbers to assign to the second value based on the position of the lowest neighbor
    numbers = [1, 2, 3, 4, 6, 7, 8, 9]
    # Get the size of the matrix
    size = len(matrix)
    # Iterate over each pixel in the matrix
    for i in range(size):
        for j in range(size):
            # Get the first value of the current pixel
            current = matrix[i][j][0]
            # Initialize the lowest value and the index of the lowest neighbor
            lowest = current
            lowest_index = -1
            # Iterate over the eight neighbors
            for k in range(8):
                # Get the coordinates of the neighbor
                x = i + offsets[k][0]
                y = j + offsets[k][1]
                # Check if the coordinates are valid (within the matrix)
                if 0 <= x < size and 0 <= y < size:
                    # Get the first value of the neighbor
                    neighbor = matrix[x][y][0]
                    # Compare the neighbor with the current pixel and the lowest value
                    if neighbor < current and neighbor < lowest:
                        # Update the lowest value and the index of the lowest neighbor
                        lowest = neighbor
                        lowest_index = k
            # Check if the lowest index is valid (not -1)
            if lowest_index != -1:
                # Assign the corresponding number to the second value of the current pixel
                matrix[i][j][1] = numbers[lowest_index]
            else:
                # Assign 5 to the second value of the current pixel if it has the lowest value among its neighbors
                matrix[i][j][1] = 5
    # Return the modified matrix
    return matrix


def modify_matrix(matrix, direction):
    # Define the offsets for the eight neighbors
    offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    # Define the numbers to assign to the second value based on the position of the lowest neighbor
    numbers = [1, 2, 3, 4, 6, 7, 8, 9]
    # Get the size of the matrix
    size = len(matrix)
    # Iterate over each pixel in the matrix
    if direction == 1:
        # Iterate over the matrix from top left to right and bottom
        for i in range(size):
            for j in range(size):
                # Get the first and second value of the current pixel
                current = matrix[i][j][2]
                position = matrix[i][j][1]
                # Check if the second value is 0 or 5, meaning no smallest neighbor
                if position == 0 or position == 5:
                    # Do nothing
                    pass
                else:
                    # Find the index of the position in the numbers list
                    index = numbers.index(position)
                    # Get the coordinates of the smallest neighbor
                    x = i + offsets[index][0]
                    y = j + offsets[index][1]
                    # Check if the coordinates are valid (within the matrix)
                    if 0 <= x < size and 0 <= y < size:
                        # Add the first value of the current pixel to the third value of the smallest neighbor
                        matrix[x][y][2] += current
    elif direction == 4:
        # Iterate over the matrix from top left to right and bottom
        for i in range(size - 1, -1, -1):
            for j in range(size - 1, -1, -1):
                # Get the first and second value of the current pixel
                current = matrix[i][j][2]
                position = matrix[i][j][1]
                # Check if the second value is 0 or 5, meaning no smallest neighbor
                if position == 0 or position == 5:
                    # Do nothing
                    pass
                else:
                    # Find the index of the position in the numbers list
                    index = numbers.index(position)
                    # Get the coordinates of the smallest neighbor
                    x = i + offsets[index][0]
                    y = j + offsets[index][1]
                    # Check if the coordinates are valid (within the matrix)
                    if 0 <= x < size and 0 <= y < size:
                        # Add the first value of the current pixel to the third value of the smallest neighbor
                        matrix[x][y][2] += current
    elif direction == 3:
        # Iterate over the matrix from top left to right and bottom
        for i in range(size - 1, -1, -1):
            for j in range(size):
                # Get the first and second value of the current pixel
                current = matrix[i][j][2]
                position = matrix[i][j][1]
                # Check if the second value is 0 or 5, meaning no smallest neighbor
                if position == 0 or position == 5:
                    # Do nothing
                    pass
                else:
                    # Find the index of the position in the numbers list
                    index = numbers.index(position)
                    # Get the coordinates of the smallest neighbor
                    x = i + offsets[index][0]
                    y = j + offsets[index][1]
                    # Check if the coordinates are valid (within the matrix)
                    if 0 <= x < size and 0 <= y < size:
                        # Add the first value of the current pixel to the third value of the smallest neighbor
                        matrix[x][y][2] += current
    elif direction == 2:
        # Iterate over the matrix from top left to right and bottom
        for i in range(size):
            for j in range(size - 1, -1, -1):
                # Get the first and second value of the current pixel
                current = matrix[i][j][2]
                position = matrix[i][j][1]
                # Check if the second value is 0 or 5, meaning no smallest neighbor
                if position == 0 or position == 5:
                    # Do nothing
                    pass
                else:
                    # Find the index of the position in the numbers list
                    index = numbers.index(position)
                    # Get the coordinates of the smallest neighbor
                    x = i + offsets[index][0]
                    y = j + offsets[index][1]
                    # Check if the coordinates are valid (within the matrix)
                    if 0 <= x < size and 0 <= y < size:
                        # Add the first value of the current pixel to the third value of the smallest neighbor
                        matrix[x][y][2] += current
    else:
        print("Invalid direction")
    # Return the modified matrix
    return matrix


# Example usage
matrix_size = 100
result_matrix = generate_matrix(matrix_size)
result_matrix = compare_matrix(result_matrix)
result_matrix = modify_matrix(result_matrix, 1)
result_matrix = modify_matrix(result_matrix, 4)
result_matrix = modify_matrix(result_matrix, 2)
result_matrix = modify_matrix(result_matrix, 3)
# Printing the result matrix
for row in result_matrix:
    print(row)
print('====================================================================================================================================================================================================================================================================================================================================')
for row in result_matrix:
    print([pixel[2] for pixel in row])

third_value_matrix = [[pixel[2] for pixel in row] for row in result_matrix]

# Define the colors and shades
colors = ["blue", "green", "yellow", "red"]
shades = [200, 1000]

# Calculate the average of the numbers in the matrix
avg = np.mean(third_value_matrix)

# Calculate the mean of the numbers less than the average
lower_mean = np.mean([x for x in np.ravel(third_value_matrix) if x < avg])

# Calculate the mean of the numbers greater than the average
upper_mean = np.mean([x for x in np.ravel(third_value_matrix) if x > avg])

# Define the thresholds that divide the numbers into four parts
thresholds = [lower_mean, avg, upper_mean]


# Define a function to map a value to a color and shade
def get_color_and_shade(value):
    # Find the index of the part that the value belongs to
    index = np.searchsorted(thresholds, value)
    # Get the color for that part
    color = colors[index]
    # Calculate the shade based on the closeness to the lower or upper limit
    if index == 0:
        # For the first part, use the lower limit as the reference
        lower_limit = 0
    else:
        # For the other parts, use the previous threshold as the reference
        lower_limit = thresholds[index - 1]
    if index == len(colors) - 1:
        # For the last part, use the maximum value as the upper limit
        upper_limit = np.max(third_value_matrix)
    else:
        # For the other parts, use the current threshold as the upper limit
        upper_limit = thresholds[index]
    # Calculate the ratio of the distance to the lower limit and the range
    ratio = (value - lower_limit) / (upper_limit - lower_limit)
    # Interpolate the shade between the minimum and maximum values
    shade = shades[0] + ratio * (shades[1] - shades[0])
    return color, shade


# Create an empty list to store the colors and shades
color_matrix = []

# Loop through the result matrix
for row in third_value_matrix:
    # Create an empty list to store the colors and shades for each row
    color_row = []
    for value in row:
        # Get the color and shade for each value
        color, shade = get_color_and_shade(value)
        # Append the color and shade to the row list
        color_row.append((color, shade))
    # Append the row list to the matrix list
    color_matrix.append(color_row)

# Convert the color matrix to a numpy array
color_matrix = np.array(color_matrix)

# Create a figure and an axis
fig, ax = plt.subplots()

# Loop through the color matrix
for i in range(color_matrix.shape[0]):
    for j in range(color_matrix.shape[1]):
        # Get the color and shade for each cell
        color, shade = color_matrix[i, j]
        # Plot a rectangle with the color and shade
        ax.add_patch(plt.Rectangle((j, i), 1, 1, color=color, alpha=(float(shade) / 1000)))

# Set the axis limits and aspect ratio
ax.set_xlim(0, color_matrix.shape[1])
ax.set_ylim(0, color_matrix.shape[0])
ax.set_aspect("equal")

# Hide the axis ticks and labels
ax.set_xticks([])
ax.set_yticks([])

# Show the plot
plt.show()
