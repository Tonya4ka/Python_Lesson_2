# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и 
# выведите на экран их сумму.
# Пример: - Для n = 4: {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} сумма 9.06
n = int(input("Type a number: "))   
sequence = {i:round((1 + 1 / i)**i,2) for i in range (1, n + 1)}  
print(sequence)

summ = 0
for k, v in sequence.items():
    summ += v
print(summ)