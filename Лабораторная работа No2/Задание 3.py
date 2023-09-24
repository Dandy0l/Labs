import numpy

a = [
    [5, 4, 3],
    [2, 4, 6],
    [4, 7, 9]
]

print(numpy.linalg.matrix_power(a, -1), '\n\nИли\n\n', numpy.linalg.inv(a))