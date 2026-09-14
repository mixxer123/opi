x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if (x1 + y1) % 2 == 0:
    color1 = "White"
else:
    color1 = "Black"

if (x2 + y2) % 2 == 0:
    color2 = "White"
else:
    color2 = "Black"

if color1 == color2:
    print(f"YES {color1}")
else:
    print("NO")
