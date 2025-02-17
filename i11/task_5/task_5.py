class IntMath:

    @staticmethod
    def pow(v: int, p: int) -> int:
        return v**p

# Do not change the code below
if __name__ == "__main__":
    assert IntMath.pow(2, 2) == 4  # Вызов статического метода через класс
    assert IntMath().pow(2, 2) == 4  # Вызов статического метода через объект
