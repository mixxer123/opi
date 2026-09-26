x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

def getQuadrant(x, y):
    if x > 0 and y > 0:
        return "I"
    elif x < 0 and y > 0:
        return "II"
    elif x < 0 and y < 0:
        return "III"
    elif x > 0 and y < 0:
        return "IV"

q1 = getQuadrant(x1, y1)
q2 = getQuadrant(x2, y2)

if q1 == q2:
    print(f"Yes, {q1}")
else:
    print("No")
