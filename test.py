import algorithm


def check(result, expected, precision):
    if result.size != expected.size: return False
    for i in range(result.size):
        if abs(expected.vector[i] - result.vector[i]) > precision:
            return False
    return True


def small_test():
    matrix = algorithm.Matrix(
        matrix=[[1, 1],
                [1, -2]],
        result=algorithm.Vector(
            vector=[0, 1],
            size=2
        ),
        size=2
    )
    precision = 0.00001
    result = algorithm.run_algorithm(matrix, precision)
    expected = algorithm.Vector(
        vector=[0.33333, -0.33333],
        size=2
    )
    assert (check(result, expected, precision))


if __name__ == '__main__':
    small_test()
