vvod = open('Дементеев Дмитрий Николаевич_УБ-32_Pr8-2-2_vvod.txt')
vivod = open('Дементеев Дмитрий Николаевич_УБ-32_Pr8-2-2_vivod.txt', 'w')

N = 4
A = []
for stroka in vvod:
    elem = []
    for l in stroka.strip().split():
        elem.append(int(l))
    A.append(elem)

for i in range(len(A)):
    A[i][0], A[i][N-1] = A[i][N-1], A[i][0]
for strok in A:
    vivod.write(str(strok))
    vivod.write('\n')