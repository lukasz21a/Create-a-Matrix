class Matrix:
    """
    Class to build a mathematical matrix.
    """
    def __init__(self, array):
        if not isinstance(array, list):
            raise TypeError('Pass a nested list to create a matrix!')
        if len(array) != 0:
            if not all(isinstance(row, list) for row in array):
                raise TypeError('Each element of the list has to be a list!')
            if not all(isinstance(number, (int, float))
                       for row in array for number in row):
                raise TypeError('Allowed values are int and float!')
            if not all(len(row) == len(array[0]) for row in array):
                raise TypeError('All columns have to be the same length!')
            if not all(len(row) for row in array):
                raise TypeError('All rows must contain at least one item!')
            self.array = array
        else:
            self.array = []

    def __repr__(self):
        return str(self.array)

    @property
    def num_of_rows(self):
        """
        Returns the number of rows of the matrix.
        """
        return len(self.array)

    @property
    def num_of_columns(self):
        """
        Returns the number of columns of the matrix.
        """
        if len(self.array) > 0:
            return len(self.array[0])
        else:
            return 0

    @property
    def size(self):
        """
        Returns the size of the matrix as a tuple.
        """
        return self.num_of_rows, self.num_of_columns

    @property
    def is_square(self):
        """
        Returns True if the matrix is square.
        If it is not square returns False.
        """
        return self.num_of_rows == self.num_of_columns

    def zero(self):
        """
        Returns a zero matrix with the size of the original matrix.
        """
        return Matrix([[0 for x in range(self.num_of_columns)]
                       for x in range(self.num_of_rows)])

    def identity(self):
        """
        Returns an identity matrix with the size of the original matrix,
        if it is square. If it is not square returns None.
        """
        if self.num_of_columns == self.num_of_rows:
            self.array = [[0 for _ in range(self.num_of_columns)]
                          for _ in range(self.num_of_rows)]
            for i in range(self.num_of_columns):
                self.array[i][i] = 1
            return Matrix(self.array)
        return None


mat = Matrix([[2, 4.0, 1], [2, -5, 2]])
print(mat)
print(mat.num_of_columns)
print(mat.num_of_rows)
print(mat.size)
print(mat.is_square)
print(mat.zero())
print(mat.identity())