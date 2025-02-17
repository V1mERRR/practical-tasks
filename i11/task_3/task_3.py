class Vehicle:
    def __init__(self, name):
        self.name = name

    def is_truck(self):
        return self.name.lower() == "truck"  # Метод возвращает True, если название автомобиля - "truck"

if __name__ == "__main__":
    # Создание объекта класса Vehicle с именем "Truck"
    c = Vehicle("Truck")

    assert isinstance(c, Vehicle)  # Проверка, что c является экземпляром класса Vehicle
    assert c.is_truck()  # Проверка, что метод is_truck() возвращает True
