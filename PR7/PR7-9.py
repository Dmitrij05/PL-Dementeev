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

mas1 = [2, 3, 5]
mas2 = [1, 7, 4]
mas3 = [6, 9, 8]


def function1(mas):
    return sum(mas) / len(mas)

def function2(mas):
    a = 1
    for i in range(len(mas)):
        a = a * mas[i]
    return a


print(f'1 массив: Среднее значение - {function1(mas1):.2f} Произведение - {function2(mas1)}')
print(f'2 массив: Среднее значение - {function1(mas2):.2f} Произведение - {function2(mas2)}')
print(f'3 массив: Среднее значение - {function1(mas3):.2f} Произведение - {function2(mas3)}')