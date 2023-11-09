##Вариант 2##
##1 часть
matrix = [[1, 2, 7],
          [1, 7, 2],
          [8, 1, 1]]
rez = 'Является'
for l in range(len(matrix)):
    summ = 0
    for i in range(len(matrix)):
        summ += matrix[i][l]
    if summ != sum(matrix[0]):
        rez = 'Не является'
for i in matrix:
    if sum(i) != sum(matrix[0]):
        rez = 'Не является'
print(rez)
## 2 часть
N = 4
A = [[2, 6, 4, 7],
     [5, 3, 8, 9],
     [7, 1, 2, 4]]
for i in range(len(A)):
    A[i][0], A[i][N-1] = A[i][N-1], A[i][0]
for strok in A:
    print(strok)