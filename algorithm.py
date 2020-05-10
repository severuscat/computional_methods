from matrix_utils import *


def check_precision(matr, vector, prec):
    v = matr.multiply_by_vector(vector).minus(matr.result)
    s = sum([x * x for x in v.vector])
    return pow(s, 1 / 2) > prec


def run_algorithm(matr, prec):
    matrix_transposed = matr.transposed()
    matr = matrix_transposed.multiply_by_matrix(matr)  # make matrix symmetric
    matr.result = matrix_transposed.multiply_by_vector(matr.result)
    x = matr.result
    while check_precision(matr, x, prec):
        a_k = matr.multiply_by_vector(x).minus(matr.result)
        alpha = a_k.scal_prod(a_k) / matr.multiply_by_vector(a_k).scal_prod(a_k)
        p = a_k.mul_by_const(-1)
        x = x.plus(p.mul_by_const(alpha))
    return x


if __name__ == "__main__":
    matrix = Matrix()
    matrix.read_matrix()
    precision = float(input())
    res = run_algorithm(matrix, precision)
    res.print_vect()
