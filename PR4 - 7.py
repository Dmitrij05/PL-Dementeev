n = int(input())
faktorial = 1
summ_faktorial = 0
for i in range(1, n + 1):
    faktorial *= i
    summ_faktorial += faktorial
print(summ_faktorial)