import math

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

max_sides = [max(one), max(two), max(three)]
min_sides = [min(one), min(two), min(three)]

def heron_area(sides):
    s = sum(sides) / 2
    area = math.sqrt(s * (s - sides[0]) * (s - sides[1]) * (s - sides[2]))
    return area

max_triangle_area = heron_area(max_sides)
min_triangle_area = heron_area(min_sides)

print(f"Площадь треугольника с максимальными сторонами: {max_triangle_area:.2f}")
print(f"Площадь треугольника с минимальными сторонами: {min_triangle_area:.2f}")
