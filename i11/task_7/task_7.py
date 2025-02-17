class Point:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other: "Point") -> "Point":
        # Возвращаем новый объект Point, сложив координаты x и y
        return Point(self.x + other.x, self.y + other.y)

# Do not change the code below
if __name__ == "__main__":
    p1 = Point(1, 1)
    p2 = Point(2, 3)

    p3 = p1 + p2  # Сложение объектов
    assert p3.x == 3  # Проверка на сумму по оси X
    assert p3.y == 4  # Проверка на сумму по оси Y
