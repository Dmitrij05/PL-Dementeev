##Вариант 7##

##Часть 1##
massiv = [11, 21, 5, 45, 58, 63, 74, 81, 92, 13]
sum_massiv = 0
proizv_massiv = 1
for i in range(len(massiv)):
    if i % 2 == 0:
        sum_massiv += massiv[i]
    else:
        proizv_massiv *= massiv[i]
print(f'Сумма:', sum_massiv)
print(f'Произведение:', proizv_massiv)

##Часть 2##
masiv = [11, 21, 5, 45, 58, 63, 74, 81, 92, 13]
max_masiv = 0
min_masiv = 0
for i in range(len(masiv)):
    if masiv[i] <= min(masiv):
        min_masiv = i
    elif masiv[i] >= max(masiv):
        max_masiv = i
masiv[max_masiv], masiv[min_masiv] = masiv[min_masiv], masiv[max_masiv]
print(f'Измененный массив:', masiv)