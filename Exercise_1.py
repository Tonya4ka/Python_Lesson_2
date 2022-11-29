# Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.
# Пример: - 6782 -> 23
# - 0,56 -> 11
number = input("Type a number: ")
sum_res = 0
lst = list(number)
for el in lst:
    if el == '.' or el == '-' or el == ',':
        continue
    sum_res += int(el)
print(sum_res)

