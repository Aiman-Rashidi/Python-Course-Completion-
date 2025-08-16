def flatten_and_double_1(matrix_1):
    matrix_2 = []
    for rows in matrix_1:
            for number in rows:
                    matrix_2.append(number)
    matrix_2 = [number*2 for number in matrix_2 if number*2 > 5]
    return matrix_2
        
def flatten_and_double_2(matrix_1):
    matrix_2 = [num*2 for rows in matrix_1 for num in rows if num*2 > 5]
    return matrix_2

matrix_1 = [
    [1, 3, 4],
    [5, 6, 7],
    [8, 2, 10]
]

print(flatten_and_double_1(matrix_1))
print(flatten_and_double_2(matrix_1))