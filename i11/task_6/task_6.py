class Person:

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

# Do not change the code below
if __name__ == "__main__":
    p = Person("Jon", "Doe")

    assert p.full_name == "Jon Doe"  # Проверка на полное имя
    assert isinstance(Person.full_name, property)  # Проверка, что full_name - это свойство
    assert "full_name" not in p.__dict__  # Проверка, что атрибут full_name не находится в словаре экземпляра
