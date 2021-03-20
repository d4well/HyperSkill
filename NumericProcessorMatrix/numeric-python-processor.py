import numpy as np

def matrix_check(matrix, m, n):
    for i in matrix:
        if len(matrix) != m or len(i) != n:
            print("ERROR")
            return False
    return True

def matrices_check(m1, n1, m2, n2):
    if m1 != m2 or n1 != n2:
        print("ERROR")
        return False
    return True

def check_number_type(num):
    if '.' in num:
        return float(num)
    else:
        return int(num)

def matrices_add():
    m1, n1 = [int(i) for i in input("Enter size of first matrix: ").split()]
    print("Enter first matrix: ")
    matrix1 = [[float(i) for i in input().split()] for i in range(m1)]
    m2, n2 = [int(i) for i in input("Enter size of second matrix: ").split()]
    print("Enter second matrix: ")
    matrix2 = [[float(i) for i in input().split()] for i in range(m2)]
    matrices = [matrix1, matrix2]
    lengths = [(m1, n1), (m2, n2)]

    def matrices_addition(matrix1, matrix2):
        new_mat = []
        for mat1, mat2 in zip(matrix1, matrix2):
            new_row = [mat1[i] + mat2[i] for i in range(len(mat1))]
            new_mat.append(new_row)
        return new_mat

    for i in zip(matrices, lengths):
        matrix_check(i[0], *i[1])

    if matrices_check(m1, n1, m2, n2):
        new_mat = matrices_addition(matrix1, matrix2)
    else:
        new_mat = []

    if new_mat:
        print("The result is:")
        for r in new_mat:
            row = [str(num) for num in r]
            print(' '.join(row))
        print("")

def matrix_const_multiplication():
    m1, n1 = [int(i) for i in input("Enter size of matrix: ").split()]
    print("Enter matrix: ")
    matrix = [[float(i) for i in input().split()] for i in range(m1)]
    const = int(input("Enter constant: "))

    def matrices_multiplication(matrix, const):
        new_mat = []
        for row in matrix:
            new_row = [i * const for i in row]
            new_mat.append(new_row)
        return new_mat

    if matrix_check(matrix, m1, n1):
        new_mat = matrices_multiplication(matrix, const)
    else:
        new_mat = []

    if new_mat:
        print("The result is:")
        for r in new_mat:
            row = [str(num) for num in r]
            print(' '.join(row))
        print("")

def matrices_multiplication():
    m1, n1 = [int(i) for i in input("Enter size of first matrix: ").split()]
    print("Enter first matrix: ")
    matrix1 = [[float(i) for i in input().split()] for i in range(m1)]
    m2, n2 = [int(i) for i in input("Enter size of second matrix: ").split()]
    print("Enter second matrix: ")
    matrix2 = [[float(i) for i in input().split()] for i in range(m2)]
    matrices = [matrix1, matrix2]
    lengths = [(m1, n1), (m2, n2)]
    m3 = [[row[i] for row in matrix2] for i in range(n2)]

    def matrices_check(m1, n1, m2, n2):
        if n1 != m2:
            print("ERROR")
            return False
        return True

    for i in zip(matrices, lengths):
        matrix_check(i[0], *i[1])

    if matrices_check(m1, n1, m2, n2):
        new_mat = [[sum([i*j for i, j in zip(row1, row2)]) for row2 in m3] for row1 in matrix1]
    else:
        new_mat = []

    if new_mat:
        print("The result is:")
        for r in new_mat:
            row = [str(num) for num in r]
            print(' '.join(row))
        print("")

def transponse_main():
    m1, n1 = [int(i) for i in input("Enter size of matrix: ").split()]
    print("Enter matrix: ")
    matrix1 = [[check_number_type(i) for i in input().split()] for i in range(m1)]

    t_matrix = [*zip(*matrix1)]

    if t_matrix:
        print("The result is:")
        for r in t_matrix:
            row = [str(num) for num in r]
            print(' '.join(row))
        print("")
        
def transponse_side():
    m1, n1 = [int(i) for i in input("Enter size of matrix: ").split()]
    print("Enter matrix: ")
    matrix1 = [[check_number_type(i) for i in input().split()] for i in range(m1)]
    m3 = [[row[i] for row in reversed(matrix1)] for i in range(n1)]
    m3.reverse()
    t_matrix = m3
    
    if t_matrix:
        print("The result is:")
        for r in t_matrix:
            row = [str(num) for num in r]
            print(' '.join(row))
        print("")

def transponse_vertical():
    m1, n1 = [int(i) for i in input("Enter size of matrix: ").split()]
    print("Enter matrix: ")
    matrix1 = [[check_number_type(i) for i in input().split()] for i in range(m1)]
    m3 = [[i for i in reversed(row)] for row in matrix1]
    t_matrix = m3
    
    if t_matrix:
        print("The result is:")
        for r in t_matrix:
            row = [str(num) for num in r]
            print(' '.join(row))
        print("")

def transponse_horizontal():
    m1, n1 = [int(i) for i in input("Enter size of matrix: ").split()]
    print("Enter matrix: ")
    matrix1 = [[check_number_type(i) for i in input().split()] for i in range(m1)]
    matrix1 = [i for i in reversed(matrix1)]
    t_matrix = matrix1
    
    if t_matrix:
        print("The result is:")
        for r in t_matrix:
            row = [str(num) for num in r]
            print(' '.join(row))
        print("")

##def determinant():
##    m1, n1 = [int(i) for i in input("Enter size of matrix: ").split()]
##    print("Enter matrix: ")
##    matrix = [[check_number_type(i) for i in input().split()] for i in range(m1)]
##    print("The result is:")
##    print(round(np.linalg.det(matrix))
        
def determinant(matrix):
    nums = []
    for num, elem in enumerate(matrix[0]):
            if num == 0:
                    n = matrix[1][1] * matrix[2][2]
                    m = matrix[1][2] * matrix[2][1]
                    nums.append(elem * (n-m))
            elif num == 1:
                    n = matrix[1][0] * matrix[2][2]
                    m = matrix[1][2] * matrix[2][0]
                    nums.append((-1 * elem) * (n-m))
            elif num == 2:
                    n = matrix[1][0] * matrix[2][1]
                    m = matrix[1][1] * matrix[2][0]
                    nums.append(elem * (n-m))
    return sum(nums)

def determinant_caller(matrix):

    cofactors = []
    
    if len(matrix[0]) == 3:
        det = determinant(matrix)
        return det
    if len(matrix[0]) == 4:
        to_det = []
        cofactors.append(matrix[0])
        m1 = [row[:] for row in matrix[1::]]
        for num, item in enumerate(matrix[0]):
            n1 = [[it for rn, it in enumerate(row) if rn != num] for row in m1]
            to_det.append(n1)
        dets = [determinant(mat) for mat in to_det]
        print(dets)
        main_det = 0
        for i, j in zip(cofactors.pop(), dets):
            main_det += i*j
        print(main_det)
        return main_det
    if len(matrix[0]) > 4:
        to_det = []
        cofactors.append(matrix[0])
        m1 = [row[:] for row in matrix[1::]]
        for num, item in enumerate(matrix[0]):
            n1 = [[it for rn, it in enumerate(row) if rn != num] for row in m1]
            to_det.append(n1)
        

def determinant_check():
    m1, n1 = [int(i) for i in input("Enter size of matrix: ").split()]
    print("Enter matrix: ")
    matrix = [[check_number_type(i) for i in input().split()] for i in range(m1)]
    
    if m1 != n1:
        print("ERROR")
    
    determinant_caller(matrix)
        
while True:
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("4. Transpose matrix")
    print("5. Calculate a determinant")
    print("0. Exit")
    user_input = int(input("Your choice: "))
    if user_input == 1:
        matrices_add()
    elif user_input == 2:
        matrix_const_multiplication()
    elif user_input == 3:
        matrices_multiplication()
    elif user_input == 4:
        print("1. Main diagonal")
        print("2. Side diagonal")
        print("3. Vertical line")
        print("4. Horizontal line")
        user_input = int(input("Your choice: "))
        if user_input == 1:
            transponse_main()
        elif user_input == 2:
            transponse_side()
        elif user_input == 3:
            transponse_vertical()
        elif user_input == 4:
            transponse_horizontal()
        else:
            continue
    elif user_input == 5:
        determinant_check()
    elif user_input == 0:
        break
    else:
        continue


        

 

