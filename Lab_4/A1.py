import random
import time

while True:
    try:
        n = int(input("Введите количество примеров: "))
        if n <= 0:
            print("Пожалуйста, введите число больше 0.")
            continue
        break
    except ValueError:
        print("Пожалуйста, введите целое число!")

correct_answers = 0
total_time = 0.0

for i in range(1, n + 1):
    a = random.randint(2, 9)
    b = random.randint(2, 9)

    correct_result = a * b
    start_time = time.time()

    print(f'Вопрос {i}/{n}')

    while True:
        user_input = input(f"{a} × {b} = ")
        try:
            user_answer = int(user_input)
        except ValueError:
            print("Пожалуйста, введите целое число!")
            continue

        time_spend = time.time() - start_time
        total_time += time_spend

        if user_answer == correct_result:
            print(f'Верно! (Время: {time_spend:.1f} сек)')
            correct_answers += 1
        else:
            print(f'Неверно! Правильно: {correct_result} (Время: {time_spend:.1f} сек)')

        break

avg_time = total_time / n if n > 0 else 0
success_percent = (correct_answers / n) * 100 if n > 0 else 0

print("=" * 50)
print("СТАТИСТИКА:")
print("=" * 50)
print(f"Общее время: {total_time:.1f} секунд")
print(f"Среднее время на вопрос: {avg_time:.1f} сек")
print(f"Правильных ответов: {correct_answers}/{n}")
print(f"Процент правильных: {success_percent:.1f}%")