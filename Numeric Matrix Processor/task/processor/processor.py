def read_matrix_size(prompt):
    return list(map(int, input(prompt).split()))


def read_matrix_rows(n_rows):
    return [list(map(float, input().split())) for _ in range(n_rows)]


def add_matrices():
    try:
        n, m = read_matrix_size('Enter size of first matrix: ')
        print('Enter first matrix:')
        a = read_matrix_rows(n)

        n, m = read_matrix_size('Enter size of second matrix: ')
        print('Enter second matrix:')
        b = read_matrix_rows(n)

        print('The result is:')
        for x in range(n):
            s = [a[x][y] + b[x][y] for y in range(m)]
            print(*s)
    except (Exception,):
        print('ERROR')


def multiply_by_const():
    n, m = list(map(int, input('Enter size of matrix: ').split()))

    print('Enter matrix:')
    a = read_matrix_rows(n)

    c = float(input('Enter constant: > '))

    print('The result is:')
    for row in a:
        s = [c * x for x in row]
        print(*s)


def multiply_matrices():
    try:
        n, m = read_matrix_size('Enter size of first matrix: ')
        print('Enter first matrix:')
        a = read_matrix_rows(n)

        m, k = read_matrix_size('Enter size of second matrix: ')
        print('Enter second matrix:')
        b = read_matrix_rows(m)

        print('The result is:')
        for x in range(n):
            s = [sum([a[x][z] * b[z][y] for z in range(m)]) for y in range(k)]
            print(*s)
    except (Exception,):
        print('ERROR')


def transpose_matrix():
    choice = int(input("""
1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line
Your choice: """))

    n, m = list(map(int, input('Enter matrix size: ').split()))

    print('Enter matrix:')
    a = read_matrix_rows(n)

    if choice == 1:
        list(map(print, *a))
    elif choice == 2:
        list(map(print, *[row[::-1] for row in a[::-1]]))
    elif choice == 3:
        list(map(lambda x: print(*x[::-1]), a))
    elif choice == 4:
        list(map(lambda x: print(*x), a[::-1]))


def det(a):
    if len(a) == 1:
        return a[0][0]
    return sum(a[i][0] * ((-1) ** i) *
               det([a[row][1:] for row in range(len(a)) if row != i])
               for i in range(len(a)))


def calculate_a_determinant():
    n, m = list(map(int, input('Enter matrix size: ').split()))

    print('Enter matrix:')
    a = read_matrix_rows(n)

    print('The result is:')
    print(det(a))


def inverse_matrix():
    try:
        n, m = read_matrix_size('Enter matrix size: ')
        print('Enter matrix:')
        a = read_matrix_rows(n)

        cofactors = [
            [
                ((-1) ** (x + y)) * det([
                    [a[col][row] for col in range(m) if col != x]
                    for row in range(n) if row != y
                ]) for x in range(m)
            ] for y in range(n)
        ]

        print('The result is:')
        c = 1 / det(a)
        for row in cofactors:
            s = [c * x for x in row]
            print(*s)
    except (Exception,):
        print("This matrix doesn't have an inverse.")


while True:
    choice = int(input("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit
Your choice: """))
    if choice == 0:
        break
    if choice == 1:
        add_matrices()
    elif choice == 2:
        multiply_by_const()
    elif choice == 3:
        multiply_matrices()
    elif choice == 4:
        transpose_matrix()
    elif choice == 5:
        calculate_a_determinant()
    elif choice == 6:
        inverse_matrix()
    print()
