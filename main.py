
def matrixMul(matrixA, matrixB):
    """
    A Function that gets 2 matrices and checks if they are: 1. Square matrix
                                                            2. In the same size
    ** If one of the two above is False the program will stop **
    Then the function will multiply them according to the according to the multiplication algorithm
    :param matrixA: The matrix at the left of the multiplication
    :param matrixB:The matrix at the right of the multiplication
    :return: A new matrix, it represents the results
    """
    if len(matrixA) == len(matrixB) and len(matrixA) == len(matrixA[0]):  # checks the sizes of the both matrices
        for i in range(len(matrixA)):  # checks if the left matrix is square
            if len(matrixA) != len(matrixA[i]):
                raise "Not NxN"
        for i in range(len(matrixB)):  # checks if the left matrix is square
            if len(matrixB) != len(matrixB[i]):
                raise "Not NxN"
        matrixC =[[0 for x in range(len(matrixA))] for y in range(len(matrixB))]  # Generating a new matrix for the result
        for i in range(len(matrixC)):  # multiplication according to the multiplication algorithm
            for j in range(len(matrixC)):
                for k in range(len(matrixC)):
                    matrixC[i][j] += matrixA[i][k] * matrixB[k][j]
        return matrixC
    else:
        raise "Not NxN / same size"

    def matrix_vectorMul(matrixA, vecA):
        """
        A function that multiplies a matrix and a vector and checks if they are: 1. Square matrix
                                                                                 2. In the same size
        ** If one of the two above is False the program will stop **
        Then the function will multiply them according to the according to the multiplication algorithm
        :param matrixA: The matrix is in the left side of the multiplication
        :param vecA: The vector is in the right side of the multiplication
        :return: A new vector, it represents the results
        """
        if len(matrixA) == len(vecA) and len(matrixA) == len(
                matrixA[0]):  # checks the size of the matrix and the vector
            for i in range(len(matrixA)):  # checks if the left matrix is square
                if len(matrixA) != len(matrixA[i]):
                    raise "Cant Multiply"
        newVec = [0 for i in range(len(vecA))]  # Generating a new vector for the result
        for i in range(len(matrixA)):  # multiplication according to the multiplication algorithm
            for j in range(len(vecA)):
                newVec[i] += matrixA[i][j] * vecA[j]
        return

    def I_matrix(A):
        """
        A function that generates a I matrix
        :param A: A matrix, used to make the I matrix the same size the parameter matrix
        :return: I matrix in the same size as the given matrix (parameter)
        """
        matrixC = [[0 for x in range(len(A))] for y in range(len(A))]
        for i in range(len(A)):
            matrixC[i][i] = 1
        return matrixC

    def copy_matrix(A):
        """
        A function that
        :param A: A matrix to copy
        :return: The new copied matrix
        """
        matrixC = [[A[y][x] for x in range(len(A))] for y in range(len(A))]
        return matrixC

    def determinant_recursive(A, total=0):
        """
        A recursive function that calculates the determinant of a given matrix
        :param A: A matrix
        :param total: A parameter used in the function that hold the current total, it's default is zero
        :return: The determinant of matrix A
        """
        indices = list(range(len(A)))
        if len(A) == 2 and len(A[0]) == 2:
            val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
            return val
        for fc in indices:
            As = copy_matrix(A)
            As = As[1:]
            height = len(As)
            for i in range(height):
                As[i] = As[i][0:fc] + As[i][fc + 1:]
            sign = (-1) ** (fc % 2)
            sub_det = determinant_recursive(As)
            total += sign * A[0][fc] * sub_det
        return total

def matrixSolve(matrix, vecB):
    """
    A function that finds the solution of a systems of linear equations
    :param matrix: A matrix that represent the values of the experiment
    :param vecB: A vector that represent the results of the experiment
    :return: A solution vector
    """
    elementary = []  # A List for all of the elementary matrices
    matrixes = []  # A List for all of the mid matrices along the solution
    matrixes.append(matrix)
    for i in range(len(matrix)):  # Checks if the matrix and the vector are in a size that we can work with
        if len(matrix) != len(matrix[i]) or len(matrix) != len(vecB):
            raise "not NxN or vector is not the same size of matrix"
    if determinant_recursive(matrix) != 0:  # Checks if there is a single solution according to the determinant
        solve = I_matrix(matrix)
        for i in range(len(matrix)):  # Applying Gauss Elimination
            temp=i
            flag=i
            while temp<len(matrix):
                if abs(matrix[temp][i])>abs(matrix[flag][i]):
                    flag=temp
                temp += 1
            if flag!=i:
                Imat=I_matrix(matrix)
                temp1=Imat[i]
                Imat[i]=Imat[flag]
                Imat[flag]=temp1
                elementary.append(Imat)
                matrix = matrixMul(Imat, matrix)
                matrixes.append(matrix)
            if matrix[i][i] == 0.0 :  # In case the pivot is 0 or a very small number
                k = i
                while k < len(matrix) and matrix[k][i] == 0:  # finding the first raw that does not have a 0 ( in the current column )
                    k += 1
                temp = solve[i]
                solve[i] = solve[k]
                solve[k] = temp
                elementary.append(solve)
                matrix = matrixMul(solve, matrix)
                matrixes.append(matrix)
            if matrix[i][i] != 1:  # In case the pivot in the current raw is not 1
                solve = I_matrix(matrix)
                solve[i][i] = 1 / matrix[i][i]
                elementary.append(solve)
                matrix = matrixMul(solve, matrix)
                matrix[i][i]=1
                matrixes.append(matrix)
            m = i + 1
            while m < len(matrix):  # Turning to zero all the rows below ( in the current column )
                if matrix[m][i] != 0 :
                    solve = I_matrix(matrix)
                    solve[m][i] = -matrix[m][i] / matrix[i][i]
                    elementary.append(solve)
                    matrix = matrixMul(solve, matrix)
                    matrixes.append(matrix)
                m = m + 1
        n = len(matrix) - 1
        while n >= 0:  # Obtaining Solution by Back Substitution
            m = n - 1
            while m >= 0:  # Turning to zero all the rows above ( in the current column )
                if matrix[m][n] != 0 :
                    solve = I_matrix(matrix)
                    solve[m][n] = -matrix[m][n] / matrix[n][n]
                    elementary.append(solve)
                    matrix = matrixMul(solve, matrix)
                    matrixes.append(matrix)
                m = m - 1
            n = n - 1
        for i in elementary:  # Multiplying all the elementary matrices with the vector ( to get the solution vector )
            vecB = matrix_vectorMul(i, vecB)
        with open("output.txt",'w') as f:
            f.write("The given matrix:\n\n")
            writeMatrix(matrixes[0],f)
            f.write("Gaussian elimination:\n\n")
            for i in range(len(elementary)):
                temp2='{}.'.format(i+1)
                f.write(temp2)
                f.write("\nElementary matrix:\n\n")
                writeMatrix(elementary[i],f)
                f.write("\n----------------------------------------------------------\n")
                f.write("\nPrevious matrix:\n\n")
                writeMatrix(matrixes[i],f)
                f.write("\n----------------------------------------------------------\n")
                f.write("\nResult of multiply:\n\n")
                writeMatrix(matrixes[i+1],f)
                f.write(f'\n------------------ end of stage {i+1} ----------------------\n\n')
            f.write("\nResult:\n\n")
            for i in range(len(vecB)):
                temp3 = f'X{i+1} = {vecB[i]} '
                f.write(temp3)

        return vecB
    else:
        raise "Error"

def printMatrix(matrix):
    """
    A function that prints a matrix
    :param matrix: A matrix to print
    :return:  No return value
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print('{: ^20}'.format(matrix[i][j]), end="")
        print('\n')

def writeMatrix(matrix,f):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            temp='{: ^22}'.format(matrix[i][j])
            f.write(temp)
        f.write('\n')


def printVector(vec):
    """
    A function that prints a vector
    :param vec: Vector to print
    :return: No return value
    """
    for i in vec:
        print(i)


def Norm_Of_A_Matrix(matrix):
    """
    A function that calculates a norm of a matrix
    :param matrix: A matrix
    :return: The value of the norm
    """
    temp = [0 for x in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            temp[i] += abs(matrix[i][j])
    return max(temp)

X = [[8, 0.0001, 5,0.5],
     [1.1213000001, 7, 6,0.365002],
    [2, 0.24524242452, 5, 0.245],
     [1,52.02222,4,5.36]]

matrixSolve(X,[2,0.123456001,45.5632,0.142005])
