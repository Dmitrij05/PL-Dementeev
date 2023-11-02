##Вариант №7##

##1 часть
x = 10
y = 12
z = 18     ##задаем переменные
t = 10

def S_rectangle(x, t):
    return x * t    ##площадь прямоугольника

def S_triangle(x, y, t):
    l = y - t
    return x * l * 0.5  ## Площадь прямоугольного треугольника

print(S_rectangle(x, t) + S_triangle(x, y, t)) ## Пощадь

##2 часть
n = int(input('Введите число:'))
def vosmer(n):
    return f'Число в восьмеричной системе: {n:0>10o}'
print(vosmer(n))