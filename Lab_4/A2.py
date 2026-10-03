def main():
    print("--- Отрисовка фигур ---")

    rows = int(input('Введите количество строк: '))
    columns = int(input('Введите количество столбцов: '))
    ch = input('Введите символ для отображения: ')

    print(f"\nПРЯМОУГОЛЬНИК {rows}x{columns}:")
    draw_rectangle(rows, columns, ch)

    print(f"\nПРАВЫЙ ТРЕУГОЛЬНИК:")
    draw_right_triangle(rows, ch)

    print(f"\nРАМКА {rows}x{columns}:")
    draw_frame(rows, columns, ch)

def draw_rectangle(rows, columns, ch):
    for i in range(rows):
        for j in range(columns):
            print(ch, end='')
        print()

def draw_right_triangle(rows, ch):
    for i in range(1, rows + 1):
        for j in range(i):
            print(ch, end='')
        print()

def draw_frame(rows, columns, ch):
    for i in range(rows):
        for j in range(columns):
            if i == 0 or i == rows - 1 or j == 0 or j == columns - 1:
                print(ch, end='')
            else:
                print(' ', end='')
        print()

if __name__ == "__main__":
    main()