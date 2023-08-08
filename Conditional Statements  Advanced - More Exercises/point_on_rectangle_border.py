x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

is_on_border = (x == x1 or x == x2) and (y1 <= y <= y2 or y2 <= y <= y1)
is_inside = x1 < x < x2 and y1 < y < y2

if is_on_border:
    print("Border")
else:
    print("Inside / Outside")

