from get_list import squared_part1, squared_part2, squared_part3
import pandas as pd

def normalize(matrix):
    # matrix is a 2x2 matrix represented as [[a, b], [c, d]]

    # Extract individual elements from the matrix
    a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]

    # Calculate the sum of all elements in the matrix
    total = a + b + c + d

    row_total = a + c


    # Calculate the elements of the new matrix

    added = a + b
    bdded = c + d
    new_c = added/total
    new_d = bdded/total
    weight = [round(new_d, 2), round(new_c, 2)]
    # print("Print A = " + str(a))
    # print("Print B = " + str(b))
    
    norm_matrix.append(weight)
    # Return the squared matrix
    return norm_matrix

def draw_table_ahp(woi_list, da_list, trees):

        
    # Initialize the data for the DataFrame
    data = {'': ['For No of People affected', 'For Damaged Area', 'Sum of weights of importance'],
            'Weight of Importance': woi_list,  # Leaving spaces as placeholders
            'Flooding in emergency rooms': da_list,
            'Trees fell on roads': trees
            }

    # Create the DataFrame
    df = pd.DataFrame(data)

    # Display the DataFrame
    print(df)

norm_matrix = []
normalize(squared_part1)

#print("This is the best of all ")
normalize(squared_part2)

normalize(squared_part3)
#print(norm_matrix)
#print(norm_matrix[0][0] + norm_matrix[0][1])



ans_da_pre = round(((norm_matrix[1][0] * norm_matrix[0][1]) + (norm_matrix[2][0] * norm_matrix[0][0])),3)
ans_da = round(ans_da_pre,2)
ans_tree = round(((norm_matrix[1][1] * norm_matrix[0][1]) + (norm_matrix[2][1] * norm_matrix[0][0])), 2)
nopa_list = [norm_matrix[0][1], norm_matrix[0][0], (norm_matrix[0][0] + norm_matrix[0][1])]
da_list = [norm_matrix[1][0], norm_matrix[2][0], ans_da]
if ans_tree > (1 - ans_da):
    ans_tree = (1 - ans_da)
trees = [norm_matrix[1][1], norm_matrix[2][1], ans_tree]
draw_table_ahp(nopa_list, da_list, trees)