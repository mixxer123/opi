while True:
    packets = input("Введите последовательность пакетов (0 и 1): ").strip()

    if len(packets) < 5:
        print("Ошибка: Длина строки должна быть не меньше 5 символов!")
        continue

    if not all(char in '01' for char in packets):
        print("Ошибка: Неверный ввод. Используйте только символы '0' и '1'!")
        continue

    break

total_packets = len(packets)
lost_packets = packets.count('0')

max_streak = 0
current_streak = 0

for packet in packets:
    if packet == '0':
        current_streak += 1
        if current_streak > max_streak:
            max_streak = current_streak
    else:
        current_streak = 0

loss_percent = (lost_packets / total_packets) * 100

if loss_percent <= 1:
    quality = "отличное качество"
elif loss_percent <= 5:
    quality = "хорошее качество"
elif loss_percent <= 10:
    quality = "удовлетворительное качество"
elif loss_percent <= 20:
    quality = "плохое качество"
else:
    quality = "критическое состояние сети"

print("\nРезультаты анализа:")
print(f"Общее количество пакетов: {total_packets}")
print(f"Количество потерянных пакетов: {lost_packets}")
print(f"Длина самой длинной последовательности потерянных пакетов: {max_streak}")
print(f"Процент потерь: {loss_percent:.1f}%")
print(f"Качество связи: {quality}")