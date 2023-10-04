n = int(input())
f1 = 1
f2 = 1
summa = 0
while n > 2:
    f1, f2 = f2, f1 + f2
    summa += f2
    n -= 1
print(summa + 2)