matrix_a = [[1,2,3],
            [9,8,7],
            [4,5,6]]

matrix_b = [[4,3,5],
            [1,3,4],
            [7,8,9]]

matrix_c = []

for row in range(len(matrix_a)):
    new_row = []
    for column in range(len(matrix_a[0])):
            new_row.append(matrix_a[row][column] + matrix_b[row][column])
    matrix_c.append(new_row)
    
for row in range(len(matrix_a)):
    if row !=1:
       print(f"{matrix_a[row]}       {matrix_b[row]}   {matrix_c[row]}")
    else: 
       print(f"{matrix_a[row]}  +    {matrix_b[row]} = {matrix_c[row]}")
    