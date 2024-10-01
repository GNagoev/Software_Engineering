import math

def triangle_s(a, b, c):
    hp = (a + b + c) / 2
    s = math.sqrt(hp * (hp - a) * (hp - b) * (hp - c))
    return s

from triangle_S import triangle_s

def main():
    a = float(input("Сторона a: "))
    b = float(input("Сторона b: "))
    c = float(input("Сторона c: "))
    if a + b > c and a + c > b and b + c > a:
        area = triangle_s(a, b, c)
        print(f"Площадь треугольника: {area:.2f}")
    else:
        print("Такой треугольник не существует.")

if __name__ == "__main__":
    main()
