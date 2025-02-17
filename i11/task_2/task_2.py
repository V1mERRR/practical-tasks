class Vehicle:
    def __init__(self, name):
        self.name = name

if __name__ == "__main__":
    # Создание объекта класса Vehicle с именем "Mercedes"
    c = Vehicle("Mercedes")

    assert isinstance(c, Vehicle)  # Проверка, что c является экземпляром класса Vehicle
    assert c.name == "Mercedes"  # Проверка, что имя автомобиля равно "Mercedes"
