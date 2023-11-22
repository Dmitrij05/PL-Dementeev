vvod = open('Дементеев Дмитрий Николаевич_УБ-32_Pr8-7-1_vvod.txt').read().strip().split()
vivod = open('Дементеев Дмитрий Николаевич_УБ-32_Pr8-7-1_vivod.txt', 'w')

massiv = []
for i in range(len(vvod)):
    elem = int(vvod[i])
    massiv.append(elem)

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
    vivod.write(str(stroka))
    vivod.write('\n')