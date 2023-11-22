vvod = open('Дементеев Дмитрий Николаевич_УБ-32_Pr8-2-1_vvod.txt')
vivod = open('Дементеев Дмитрий Николаевич_УБ-32_Pr8-2-1_vivod.txt', 'w')

matrix = []
for stroka in vvod:
    elem = []
    for l in stroka.strip().split():
        elem.append(int(l))
    matrix.append(elem)

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

vivod.write(rez)