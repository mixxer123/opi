import os
import math

def calculate(input_path, output_path):

    if not os.path.exists(input_path):
        print(f"Файл {input_path} не найден.")
        return

    with open(input_path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f.read().splitlines() if line.strip()]

    data_lines = lines[2:]

    times = []
    wc_temps = []
    wc_effects = []

    for line in data_lines:
        parts = line.split()
        time = parts[0]
        temp = float(parts[1])
        wind = float(parts[2])

        twc = 35.74 + 0.6125 * temp + (0.4275 * temp - 35.75) * (wind ** 0.16)
        effect = twc - temp

        times.append(time)
        wc_temps.append(twc)
        wc_effects.append(effect)

    total = 0.0
    for t in wc_temps:
        total = total + t
    average = total / len(wc_temps)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(f"{'Time':<4}{'WC temp':>12}{'WC Effect':>14}\n")
        f.write("-" * 30 + "\n")
        for i in range(len(times)):
            f.write(f"{times[i]:<8}{wc_temps[i]:>8.1f}{wc_effects[i]:>14.1f}\n")
        f.write("-" * 30 + "\n\n")
        f.write(f"The average adjusted temperature, based on {len(times)} observations, was {average:.1f}\n")


calculate('1.WCData.txt', '1.WindChillReport.txt')
