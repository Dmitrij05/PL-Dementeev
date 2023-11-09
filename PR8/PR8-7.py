## 7 вариант##
## 1 часть
massiv = [2, 1, 4, 3, 6, 5, 1, 3, 5, 7]

n = int((2 * len(massiv)) ** 0.5) # Определяем размерность матрицы
matrix = []
for i in range(n):
    matrix.append([0] * n)
index = 0
for i in range(n):
    for j in range(i, n):
        matrix[i][j] = massiv[index]
        matrix[j][i] = massiv[index]
        index += 1
for stroka in matrix:
    print(stroka)

## 2 Часть
matritsa = [[5, 3, 7],
            [1, 12, 2],
            [8, 4, 6]]
diagonali = [matritsa[i][i] for i in range(len(matritsa))]
sled = sum(diagonali)
for i in range(len(matritsa)):
    if i % 2 == 0:
        for j in range(len(matritsa[i])):
            matritsa[i][j] /= sled
for strok in matritsa:
    print(strok)