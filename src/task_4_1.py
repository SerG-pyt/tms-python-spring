# Homework - 04
# task_4_1: Дан список целых чисел. Создать новый список, каждый
# элемент которого равен исходному элементу умноженному на -2

l1 = [1, 3, 5, 7, 9, 11]
l2 = []
while l1:
    l2.append(l1.pop(0) * 2)
print(f"Удвоенный список 1: {l2}")

s1 = [1, 3, 5, 7, 9, 11]
s2 = []
for i in s1:
    s2.append(i * 2)
print(f"Удвоенный список 2: {s2}")