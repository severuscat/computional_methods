import algorithm


def check(result, expected, precision):
    if result.size != expected.size: return False
    for i in range(result.size):
        if abs(expected.get(i) - result.get(i)) > precision:
            return False


def small_test():
    matrix = algorithm.Matrix(
        matrix=[[1, 1],
                [1, -2]],
        result=[0, 1],
        size=2
    )
    precision = 0.00001
    result = algorithm.run_algorithm(matrix, precision)
    expected = algorithm.Vector(
        vector=[0.3333, -0.3333],
        size=2
    )
    assert (check(result, expected, precision))


if __name__ == '__main__':
    small_test()
