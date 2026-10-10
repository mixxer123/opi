import math


def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def get_days_in_month(month: str, year: int) -> int:
    month_days = {
        "January": 31,
        "February": 29 if is_leap_year(year) else 28,
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31,
    }
    return month_days.get(month, 0)


def process_precipitation_data():
    input_filename = "Precip.txt"
    output_filename = "Report.txt"

    with open(input_filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # заголовки
    project_header = lines[0].strip()
    station_location = lines[1].strip()
    month_year_line = lines[2].strip()

    month_part, year_part = [part.strip() for part in month_year_line.split(",")]
    month = month_part
    year = int(year_part)

    total_days = get_days_in_month(month, year)
    if total_days == 0:
        raise ValueError(f"Неизвестный месяц: {month}")

    daily_precip = {}
    errors = []

    # обработка записей по дням
    for line_idx, raw_line in enumerate(lines[3:], start=4):
        line = raw_line.strip()
        if not line:
            continue

        parts = line.split()
        if len(parts) < 2:
            continue

        day = int(parts[0])
        amount = float(parts[1])

        # проверка дня и повторений
        if day < 1 or day > total_days:
            errors.append(("Invalid", day, line_idx))
        elif day in daily_precip:
            errors.append(("Repeated", day, line_idx))
        else:
            daily_precip[day] = amount

    # расчёт статистики
    valid_count = len(daily_precip)
    if valid_count > 0:
        min_precip = min(daily_precip.values())
        max_precip = max(daily_precip.values())
        avg_precip = sum(daily_precip.values()) / total_days
    else:
        min_precip = max_precip = avg_precip = None

    with open(output_filename, "w", encoding="utf-8") as out:
        out.write("Programmer: Vladislav Gaidukov\n")
        out.write(f"{project_header}\n\n")
        out.write(
            f"Precipitation report for {station_location} during {month}, {year}\n\n"
        )

        # ошибки
        if errors:
            out.write("Error        Day     Line\n")
            for err_type, err_day, err_line in errors:
                out.write(f"{err_type:<13}{err_day:>3}{err_line:>9}\n")
            out.write("\n")

        # гистограмма
        out.write("Day Amount Graph\n")
        for day in range(1, total_days + 1):
            if day in daily_precip:
                val = daily_precip[day]
                amount_str = f"{val:>.2f}"
                if val > 0.0:
                    stars_count = math.ceil(round(val, 4) / 0.25)
                    graph_str = f" {'*' * stars_count}"
                else:
                    graph_str = ""
            else:
                amount_str = "NA"
                graph_str = ""

            out.write(f"{day:>3}{amount_str:>7}{graph_str}\n")
        out.write("\n")

        # сводка
        out.write("Minimum      Maximum      Average\n")
        if valid_count == 0:
            out.write(f"{'NA':>7}      {'NA':>7}      {'NA':>7}\n")
        else:
            out.write(
                f"{min_precip:>7.2f}      {max_precip:>7.2f}      {avg_precip:>7.2f}\n"
            )


if __name__ == "__main__":
    process_precipitation_data()
