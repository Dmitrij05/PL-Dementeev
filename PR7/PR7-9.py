##Вариант №9##
## 1 часть
number = int(input('Введите число:'))

def function(number):
    kol_deist = 0
    while number != 0:
        summa = 0
        strok_num = str(number)
        for i in range(len(strok_num)):
            summa = int(strok_num[i]) + summa
        number = number - summa
        kol_deist += 1
    return kol_deist

print(f'Количество действий =', function(number))

## 2 часть

mas1 = [1, 2, 3]
mas2 = [4, 5, 6]
mas3 = [7, 8, 9]


def function1(mas):
    a = 1
    for i in range(len(mas)):
        a = a * int(str(mas[i]))
    return a


def function2(mas):
    l = 0
    for i in range(len(mas)):
        l = l + int(str(mas[i]))
    return l / len(mas)

print(function1(mas1), function1(mas2), function1(mas3))
print(function2(mas1), function2(mas2), function2(mas3))

