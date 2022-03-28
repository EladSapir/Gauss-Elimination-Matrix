
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
