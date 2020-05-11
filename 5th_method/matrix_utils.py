class Vector:
    def __init__(self, vector=[], size=0):
        self.vector = vector
        self.size = len(vector)

    def get(self, ind):
        return self.vector[ind]

    def append(self, x):
        self.vector.append(x)
        self.size += 1

    def scal_prod(self, other):
        return sum([self.vector[i] * other.vector[i] for i in range(self.size)])

    def plus(self, other):
        return Vector([self.vector[i] + other.vector[i] for i in range(self.size)])

    def minus(self, other):
        return Vector([self.vector[i] - other.vector[i] for i in range(self.size)])

    def mul_by_const(self, k):
        return Vector([el * k for el in self.vector])

    def print_vect(self):
        print(self.vector)


class Matrix:
    def __init__(self, matrix=[], size=0, result=Vector()):
        self.size = size
        self.matrix = matrix
        self.result = result

    def read_matrix(self):
        self.size = int(input())
        for i in range(self.size):
            m = [float(k) for k in input().split()]
            self.matrix.append(m[:-1])
            self.result.append(m[-1])

    def transposed(self):
        return Matrix(matrix=[[self.matrix[j][i] for j in range(self.size)]
                       for i in range(self.size)], size=self.size, result=self.result)

    def multiply_by_matrix(self, other):
        c = Matrix()
        c.size = self.size
        c.matrix = [[
            (sum(
                [self.matrix[i][k] * other.matrix[k][j]
                 for k in range(self.size)])
            ) for j in range(self.size)] for i in range(self.size)]
        c.result = self.result
        return c

    def multiply_by_vector(self, vector):
        v = Vector()
        v.size = self.size
        v.vector = [(sum(
            [self.matrix[i][j] * vector.get(j) for j in range(self.size)]))
            for i in range(self.size)]
        return v

    def print_mat(self):
        print('[')
        for s in self.matrix:
            print(str(s))
        print(']')
