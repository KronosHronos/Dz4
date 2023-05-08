n = int(input("Введите количество элементов первого множества: "))
m = int(input("Введите количество элементов второго множества: "))

set1 = set()
set2 = set()

print("Введите элементы первого множества:")
for i in range(n):
    num = int(input())
    set1.add(num)

print("Введите элементы второго множества:")
for i in range(m):
    num = int(input())
    set2.add(num)

elements = sorted(set1.intersection(set2))
print("Числа, которые встречаются в обоих наборах:")
for num in elements:
    print(num, end=' ')
