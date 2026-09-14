a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

result = ["YES", "NO"]
index = min(a % b, 1)
print(result[index])
