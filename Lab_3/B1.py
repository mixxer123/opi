INPUT_FILE = "5.ChaseData.txt"

# перемещение по сетке
def wrap(pos, size):
    return ((pos - 1) % size) + 1

# форматирование координат
def format_pos(pos):
    if pos is None:
        return "( ?, ?)"
    row, col = pos
    return f"({row:2d},{col:2d})"


def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        raw_lines = [line.split() for line in f if line.strip() != ""]

    rows = int(raw_lines[0][0])
    cols = int(raw_lines[0][1])

    cat = None
    mouse = None

    cat_distance = 0
    mouse_distance = 0

    caught = False

    # сюда кароче будем складывать строки будущей таблицы
    table_rows = []

    for parts in raw_lines[1:]:
        command = parts[0]

        if command == "M":
            dr = int(parts[1])
            dc = int(parts[2])

            if mouse is None:
                # стартовая позиция мыши
                mouse = (dr, dc)
            else:
                # ход мыши
                old_r, old_c = mouse
                new_r = wrap(old_r + dr, rows)
                new_c = wrap(old_c + dc, cols)
                mouse_distance += abs(dr) + abs(dc)
                mouse = (new_r, new_c)

        elif command == "C":
            dr = int(parts[1])
            dc = int(parts[2])

            if cat is None:
                # стартовая позиция кота
                cat = (dr, dc)
            else:
      		# ход кота
                old_r, old_c = cat
                new_r = wrap(old_r + dr, rows)
                new_c = wrap(old_c + dc, cols)
                cat_distance += abs(dr) + abs(dc)
                cat = (new_r, new_c)

        elif command == "P":
            if cat is not None and mouse is not None:
                distance = abs(cat[0] - mouse[0]) + abs(cat[1] - mouse[1])
            else:
                distance = None
	    # записываем принты в таблицу
            table_rows.append((cat, mouse, distance))

        # проверка окончания игры
        if cat is not None and mouse is not None and cat == mouse:
            caught = True
            end_pos = cat
            break

    # вывод
    print("Cat and Mouse")
    print()
    print(f"  {'Cat':<11}{'Mouse':<11}{'Distance':>8}")
    print("-" * 32)

    for cat_pos, mouse_pos, distance in table_rows:
        distance_str = "" if distance is None else str(distance)
        print(f"{format_pos(cat_pos):<12}{format_pos(mouse_pos):<9}{distance_str:>8}")

    print("-" * 32)
    print()
    print()
    print(f"{'Distance':<12}{'Mouse':>8}{'Cat':>8}")
    print(f"{'':<12}{mouse_distance:>8}{cat_distance:>8}")
    print()

    if caught:
        print(f"Mouse caught at: {format_pos(end_pos)}")
    else:
        print("Mouse evaded Cat")


if __name__ == "__main__":
    main()
