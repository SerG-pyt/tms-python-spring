# Homework - 04
# task_4_2: Дан список целых чисел. Подсчитать сколько четных чисел в списке.

l1 = [1, 2, 3, 4, 5, 6, 8]
ch = 0
while l1:
    if l1.pop() % 2 == 0:
        ch += 1
print(f"Четных чисел в списке 1: {ch}")

s1 = [1, 2, 3, 4, 5, 6, 8, 10]
ch2 = 0
for i in s1:
    if i % 2 == 0:
        ch2 += 1
print(f"Четных чисел в списке 2: {ch2}")