vvod = open('Дементеев Дмитрий Николаевич_УБ-32_Pr8-7-2_vvod.txt')
vivod = open('Дементеев Дмитрий Николаевич_УБ-32_Pr8-7-2_vivod.txt', 'w')

matritsa = []
for stroka in vvod:
    elem = []
    for l in stroka.strip().split():
        elem.append(int(l))
    matritsa.append(elem)

diagonali = [matritsa[i][i] for i in range(len(matritsa))]
sled = sum(diagonali)
for i in range(len(matritsa)):
    if i % 2 == 0:
        for j in range(len(matritsa[i])):
            matritsa[i][j] /= sled

for strok in matritsa:
    vivod.write(str(strok))
    vivod.write('\n')