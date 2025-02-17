from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def speak(self) -> str:
        """What does the Animal say?

        Returns:
            str: the sound that the animal makes
        """

class Dog(Animal):
    def speak(self) -> str:
        return "woof"  # Реализация метода speak для собаки

class Cat(Animal):
    def speak(self) -> str:
        return "meow"  # Реализация метода speak для кошки

if __name__ == "__main__":
    assert Dog().speak() == "woof"  # Проверка для собаки
    assert Cat().speak() == "meow"  # Проверка для кошки
