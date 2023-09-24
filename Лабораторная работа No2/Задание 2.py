import numpy

def result(a):
    for res in a:
        print(res)

print('Транспонирование матрицы')
a = [
    [5, 3, 4],
    [4, 6, 10],
    [1, 2, 4]
]

b = numpy.transpose(a)
result(b)

print('\nУмножение матриц')
a = [
    [5, 4, 3],
    [2, 4, 6],
    [4, 7, 9]
]

b = [
    [3, 2, 4],
    [4, 3, 6],
    [2, 7, 5]
]

c = numpy.matmul(a, b)
result(c)

print('\nРанг матрицы')
print(numpy.linalg.matrix_rank(a))