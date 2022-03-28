
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