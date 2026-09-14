import os

def calculate(file_path, user_name):
    if not os.path.exists(file_path):
        print(f"Файл {file_path} не найден.")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f.read().splitlines() if line.strip()]

    first_line = lines[0].split()
    num_locs = int(first_line[0])
    scale = float(first_line[1])

    inches_dists = [float(x) for x in lines[1:]]

    print(user_name)
    print("Simple Map Distance Computations\n")
    print(f"Map Scale Factor:    {scale:.2f} miles per inch\n")
    print("      Map       Mileage")
    print("      Measure   Distance")
    print("=============================================")

    total_miles = 0.0

    for i in range(len(inches_dists)):
        inch = inches_dists[i]
        miles = round(inch * scale, 1)
        total_miles = total_miles + miles
        print(f"#  {i+1:<5}{inch:<10.1f}{miles:.1f}")

    print("=============================================")
    print(f"Total Distance:    {total_miles:.1f} miles")


calculate('inmap0.dat', 'Vladislav Gaidukov')
