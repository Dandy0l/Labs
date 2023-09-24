def result(a):
    for res in a:
        print(res)

print('Транспонирование матрицы')
a = [
    [5, 3, 4],
    [4, 6, 10],
    [1, 2, 4]
]

transp_result = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

for first in range(len(a)):
    for second in range(len(a[0])):
        transp_result[second][first] = a[first][second]
result(transp_result)

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

multiplication_res = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

for i in range(len(a)):
    for g in range(len(b[0])):
        for f in range(len(b)):
            multiplication_res[i][g] += a[i][f] * b[f][g]
result(multiplication_res)

print('\nНахождение ранга матрицы')
# ???????????????
