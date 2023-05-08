from random import randint

n = int(input("Введите количество кустов: "))
berries = [randint(1, 78) for i in range(n)]
print(berries)

max_berries = 0
for i in range(n):
    total_berries = berries[i] + berries[(i + 1) % n] + berries[(i + 2) % n]
    max_berries = max(max_berries, total_berries)

print("Максимальное число ягод, которое может собрать собирающий модуль:", max_berries)


