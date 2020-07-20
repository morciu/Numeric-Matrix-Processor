from copy import deepcopy


def matrix_addition():
    A = matrix_addition_1_input()
    B = matrix_addition_2_input()
    result = []
    if len(A) != len(B):
        print("ERROR")
    elif len(A) == 1:
        for i in range(len(A[0])):
            addition = A[0][i] + B[0][i]
            result.append(addition)
        print('The result is:')
        print(*result)
    else:
        for i in range(len(A)):
            row = []
            for j in range(len(B[0])):
                addition = A[i][j] + B[i][j]
                row.append(addition)
            result.append(row)
        print('The result is:')
        for x in result:
            print(*x)


def matrix_addition_1_input():
    mtx_input = input('Enter size of first matrix: ')
    try:
        mtx_dim = [int(i) for i in mtx_input.split()]
    except ValueError:
        mtx_dim = [float(i) for i in mtx_input.split()]
    matrix = []
    print('Enter first matrix:')
    for i in range(mtx_dim[0]):
        row_input = input()
        try:
            i = [int(j) for j in row_input.split()]
        except ValueError:
            i = [float(j) for j in row_input.split()]
        matrix.append(i)
    return matrix


def matrix_addition_2_input():
    mtx_input = input('Enter size of second matrix: ')
    try:
        mtx_dim = [int(i) for i in mtx_input.split()]
    except ValueError:
        mtx_dim = [float(i) for i in mtx_input.split()]
    matrix = []
    print('Enter second matrix:')
    for i in range(mtx_dim[0]):
        row_input = input()
        try:
            i = [int(j) for j in row_input.split()]
        except ValueError:
            i = [float(j) for j in row_input.split()]
        matrix.append(i)
    return matrix


def matrix_mult_input():
    mtx_input = input('Enter size of matrix: ')
    mtx_dim = [int(i) for i in mtx_input.split()]
    matrix = []
    print('Enter matrix:')
    for i in range(mtx_dim[0]):
        row_input = input()
        i = [float(j) for j in row_input.split()]
        matrix.append(i)
    return matrix


def matrix_constant_multiplication(mtx, nr):
    result = []
    for i in range(len(mtx)):
        row = []
        for j in range(len(mtx[i])):
            multiplication = mtx[i][j] * nr
            row.append(multiplication)
        result.append(row)
    return result


def matrix_multiplication():
    A = matrix_addition_1_input()
    B = matrix_addition_2_input()
    if len(A[0]) != len(B):
        print('The operation cannot be performed.')
    else:
        C = []
        B_collumns = []
        for i in range(len(B[0])):
            collumn = []
            for j in range(len(B)):
                collumn.append(B[j][i])
            B_collumns.append(collumn)
        for i in range(len(A)):
            row = []
            for j in range(len(B_collumns)):
                nr = 0
                for x in range(len(B_collumns[j])):
                    mult = B_collumns[j][x] * A[i][x]
                    nr += mult
                row.append(nr)
            C.append(row)
        print('The result is:')
        for row in C:
            print(*row)


def transpose():
    print('1. Main diagonal')
    print('2. Side diagonal')
    print('3. Vertical line')
    print('4. Horizontal line')
    trans_choice = input('Your choice: ')
    if trans_choice == '1':
        A = matrix_addition_1_input()
        print('The result is:')
        for row in trans_main_diagonal(A):
            print(*row)
    elif trans_choice == '2':
        trans_side_diagonal()
    elif trans_choice == '3':
        trans_vertical_line()
    elif trans_choice == '4':
        trans_horizontal_line()


def trans_main_diagonal(mtx):
    mtx_collumns = []
    for i in range(len(mtx[0])):
        collumn = []
        for j in range(len(mtx)):
            collumn.append(mtx[j][i])
        mtx_collumns.append(collumn)
    return mtx_collumns

def trans_side_diagonal():
    A = matrix_addition_1_input()
    A_sd_transp = []
    for i in range(len(A)-1, -1, -1):
        row = []
        for j in range(len(A[i])-1, -1, -1):
            row.append(A[j][i])
        A_sd_transp.append(row)
    print('The result is: ')
    for row in A_sd_transp:
        print(*row)


def trans_vertical_line():
    A = matrix_addition_1_input()
    A_vertical_transp = []
    for row in A:
        reverse_row = reversed(row)
        A_vertical_transp.append(reverse_row)
    print('The result is: ')
    for row in A_vertical_transp:
        print(*row)


def trans_horizontal_line():
    A = matrix_addition_1_input()
    A_horizontal_transp = reversed(A)
    print('The result is: ')
    for row in A_horizontal_transp:
        print(*row)


def determinant(mtx):
    if len(mtx) == 1:
        det_result = mtx[0][0]
        return det_result
    elif len(mtx) == 2 and len(mtx[0]) == 2:
        det_result = (mtx[0][0] * mtx[1][1]) - (mtx[1][0] * mtx[0][1])
        return det_result
    elif len(mtx) > 2 and len(mtx[0]) > 2:
        minor_mtx = deepcopy(mtx)
        del minor_mtx[0]
        list_of_minors = []
        for i in range(len(minor_mtx[0])):
            for j in range(len(minor_mtx)):
                minor_mtx[j].pop(i)
            list_of_minors.append(minor_mtx)
            minor_mtx = deepcopy(mtx)
            del minor_mtx[0]
        cofactor = 1
        determinants = []
        for minor in list_of_minors:
            mult_result = determinant(minor) * ((-1) ** (1 + cofactor))
            cofactor += 1
            determinants.append(mult_result)
        det_result = 0
        for i in range(len(mtx[0])):
            mult = mtx[0][i] * determinants[i]
            det_result += mult
        return det_result


def inverse_matrix(mtx):
    det = determinant(mtx)
    cofactor_mtx = find_cofactors(mtx)
    trans_cofactor_mtx = trans_main_diagonal(cofactor_mtx)
    constant = 1 / determinant(mtx)
    raw_inverse_mtx = matrix_constant_multiplication(trans_cofactor_mtx, constant)
    inverse_mtx = []
    for i in range(len(raw_inverse_mtx)):
        row = []
        for j in range(len(raw_inverse_mtx[i])):
            element = round(raw_inverse_mtx[i][j], 3)
            if element == -0.0:
                element = 0
            row.append(element)
        inverse_mtx.append(row)
    return inverse_mtx

def find_cofactors(mtx):
    cofactor_mtx = []
    row_position = 1
    for i in range(len(mtx)):
        minor_mtx = deepcopy(mtx)
        del minor_mtx[i]
        row = []
        for j in range(len(mtx)):
            minor_mtx = deepcopy(mtx)
            del minor_mtx[i]
            for x in range(len(minor_mtx)):
                minor_mtx[x].pop(j)
            row.append(determinant(minor_mtx))
        position_exponent = 1
        cofactor_row = []
        for x in row:
            x = x * ((-1) ** (row_position + position_exponent))
            position_exponent +=1
            cofactor_row.append(x)
        cofactor_mtx.append(cofactor_row)
        row_position += 1
    return cofactor_mtx

            




def show_menu():
    print('1. Add matrices')
    print('2. Multiply matrix by a constant')
    print('3. Multiply matrices')
    print('4. Transpose matrix')
    print('5. Calculate a determinant')
    print('6. Inverse matrix')
    print('0. Exit')

while True:
    show_menu()
    choice = input('Your choice: ')

    if choice == '1':
        matrix_addition()
    elif choice == '2':
        A = matrix_mult_input()
        constant = float(input('Enter constant: '))
        multiplication_result = matrix_constant_multiplication(A, constant)
        print('The result is:')
        for row in multiplication_result:
            print(*row)

    elif choice == '3':
        matrix_multiplication()
    elif choice == '4':
        transpose()
    elif choice == '5':
        A = matrix_mult_input()
        print('The result is:')
        print(determinant(A))
    elif choice == '6':
        A = matrix_mult_input()
        if determinant(A) == 0:
            print("This matrix doesn't have an inverse.")
        else:
            inverse_mtx = inverse_matrix(A)
            print('The result is:')
            for row in inverse_mtx:
                print(*row)
    elif choice == '0':
        break