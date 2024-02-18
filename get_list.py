import numpy as np


def get_params_er(num_people_affected_soi, damaged_area_soi):
    #print("This is the scenario for flooding in Emergency rooms. Please enter the values below. ")
    num_people_affected_er = 40
    people_affected_scale_er = 2
    damaged_area_er = 15
    damaged_area_scale_er = 4


    #print("This is the scenario for trees fell on the road. Please enter the values below. ")

    num_people_affected_trees = 80
    people_affected_scale_trees = 3
    damaged_area_trees = 25
    damaged_area_scale_trees = 5
    #print("Accroding to scale of importance (SOI) from table 6, the values are  ")
    #num_people_affected_soi = int(input("Please enter the vales for the NOPA;"))
    #damaged_area_soi = int(input("Please enter the vales for the DA:"))

    values = [[round((num_people_affected_soi/num_people_affected_soi), 2), round((damaged_area_soi/num_people_affected_soi), 2)], [round((num_people_affected_soi/damaged_area_soi), 2), round((damaged_area_soi/damaged_area_soi), 2)]]

    return values



def square_matrix(matrix):
    return np.dot(matrix, matrix)

def input_matrix(size=(2, 2)):
    """
    Asks the user to input the elements of a matrix of a given size.

    Parameters:
    - size: a tuple indicating the size of the matrix (rows, columns).

    Returns:
    - A numpy array representing the inputted matrix.
    """
    matrix = np.zeros(size)  # Initialize a matrix of zeros with the given size.
    for i in range(size[0]):  # Loop over rows
        for j in range(size[1]):  # Loop over columns
            # Ask the user to input the element at position (i, j)
            matrix[i, j] = float(input(f"Enter element [{i}, {j}]: "))
    return matrix

def create_matrix_from_values(values):
    """
    Creates a matrix from a given list of lists.

    Parameters:
    - values: A list of lists where each sublist represents a row in the matrix.

    Returns:
    - A numpy array representing the created matrix.
    """
    # Convert the list of lists into a numpy array
    matrix = np.array(values)
    return matrix

# Example usage
#values = get_params_er()
#matrix = create_matrix_from_values(get_params_er())
#matrix3 = create_matrix_from_values(values3)
#print(matrix)



def normalize_matrix(matrix):
    norm = np.linalg.norm(matrix)
    if norm == 0:
        return matrix  # Return the original matrix if norm is 0 to avoid division by 0
    return matrix / norm


# # Input matrices
# print("Input matrix 1:")
matrix1 = create_matrix_from_values(get_params_er(3,5))
# print("Input matrix 2:")
matrix2 = create_matrix_from_values(get_params_er(2,3))
# print("Input matrix 3:")
matrix3 = create_matrix_from_values(get_params_er(4,5))

# Concatenate matrices vertically
#part1, part2, part3 = concatenate_matrices(matrix1, matrix2, matrix3, axis=0)

# Now you have three variables part1, part2, and part3 for manipulation.
#print ("here: ", part1)

# Function to square a matrix using matrix multiplication


# Now square the concatenated matrix
squared_part1 = square_matrix(matrix1)
squared_part2 = square_matrix(matrix2)
squared_part3 = square_matrix(matrix3)

# Print the squared matrix
# print("Squared Part 1: " + str(squared_part1))
# print("Squared Part 2: " + str(squared_part2))
# print("Squared Part 3: " + str(squared_part3))

# normalized_part1 = normalize_matrix(squared_part1)
# normalized_part2 = normalize_matrix(squared_part2)
# normalized_part3 = normalize_matrix(squared_part3)

# print("Normalized Part 1: " + str(normalized_part1))
# print("Normalized Part 2: " + str(normalized_part2))
# print("Normalized Part 3: " + str(normalized_part3))