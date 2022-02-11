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

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError('Cannot compare an object that is not a matrix.')
        return self.array == other.array

    def __ne__(self, other):
        return not self.__eq__(other)

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError('The object passed has to be a Matrix type.')
        if not self.size == other.size:
            raise ValueError('The matrices must have the same size.')
        for i in range(self.num_of_rows):
            for j in range(self.num_of_columns):
                self.array[i][j] += other.array[i][j]
        return self.array

    def __sub__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError('Cannot subtract an object that is not a matrix.')
        if self.size != other.size:
            raise ValueError('The matrices must have the same size.')
        array = [[self.array[i][j] - other.array[i][j]
                  for j in range(self.num_of_columns)] for i in range(self.num_of_rows)]
        return Matrix(array)

    def __mul__(self, other):
        """
        Matrix multiplication.
        """
        result = [[] for _ in range(self.num_of_rows)]
        col = [[] for _ in range(other.num_of_columns)]
        for i in range(other.num_of_columns):
            for j in range(other.num_of_rows):
                col[i].append(other.array[j][i])
        for i in range(self.num_of_rows):
            for j in range(other.num_of_columns):
                result[i].append(Matrix.dot(self.array[i], col[j]))
        return Matrix(result)

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

    def add_row(self, row, index=None):
        """
        Adds a new row to the matrix. By default the row will be added
        as a last row in the matrix. It is possible to change the position
        of the row with the index parameter.
        """
        if not isinstance(row, list):
            raise TypeError('The row has to be a list.')
        if not all(type(number) in (int, float) for number in row):
            raise TypeError('All the numbers have to be of type int or float.')
        if not len(row) == self.num_of_columns:
            raise ValueError('The row length must be the same as the'
                             ' number of columns in the matrix.')
        if index is None:
            self.array.append(row)
        else:
            self.array.insert(index, row)

    def add_col(self, column, index=None):
        """
        Adds a new column to the matrix. By default the column will be
        added as a last column in the matrix. It is possible to change
        the position of the column with the index parameter.
        """
        if not isinstance(column, list):
            raise TypeError('The row has to be a list.')
        if not all(type(number) in (int, float) for number in column):
            raise TypeError('All the numbers have to be of type int or float.')
        if not len(column) == self.num_of_rows:
            raise ValueError('The row length must be the same as the '
                             'number of columns in the matrix.')
        if index is None:
            for i in range(self.num_of_rows):
                self.array[i].append(column[i])
        else:
            for i in range(self.num_of_rows):
                self.array[i].insert(index, column[i])

    def transpose(self):
        """
        Returns a transposed matrix.
        """
        row = [[] for _ in range(self.num_of_rows)]
        for j in range(self.num_of_rows):
            for i in range(self.num_of_columns):
                row[j].append(self.array[i][j])
        return Matrix(row)

    def multiply_elementwise(self, other):
        """
        Returns a resultant matrix of element-by-element multiplication. That
        is different from regular matrix multiplication, where dot products of
        rows and columns are calculated.
        """
        if not isinstance(other, Matrix):
            raise TypeError('Cannot multiply an object that is not a matrix.')
        if self.size != other.size:
            raise ValueError('The matrices must have the same size.')
        array = [[self.array[i][j] * other.array[i][j]
                  for j in range(self.num_of_columns)] for i in range(self.num_of_rows)]
        return Matrix(array)

    @classmethod
    def dot(cls, row, column):
        """
        Returns the dot product (scalar product) of two vectors.
        This class method is used for matrix multiplication.
        """
        if not isinstance((row or column), list):
            raise TypeError('Row and column must be of list type.')
        result = [row[i] * column[i] for i in range(len(row))]
        return sum(result)


mat = Matrix([[2, 4.0, 1], [2, -5, 2]])
mat2 = Matrix([[1, 2], [3, 4]])
mat.add_row([1, 2, 4])
mat.add_col([7, 7, 77])
print(mat)
print(mat.num_of_columns)
print(mat.num_of_rows)
print(mat.size)
print(mat.is_square)
print(mat.zero())
print(mat.identity())
print(mat == mat2)

mat3 = Matrix([[1, 3, -2], [4, 0, -7]])
mat4 = Matrix([[3, 2], [0, -2]])
print(mat2 * mat3)
print(mat2 + mat4)