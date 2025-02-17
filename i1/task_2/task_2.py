if __name__ == "__main__":
    # Do not change the 3 lines below
    a = "name"
    b = "is"
    my = "my"

    # Modify variables `name` and `msg` to make this script work without errors
    name = f"{my} {a}"  # создаем строку из переменных a и my
    msg = f"My name is {name}"  # создаем строку с переменной name

    # Do not change the line below
    assert msg == f"My name is {name}"  # Проверяем правильность строки

    # Выводим результат
    print(msg)  # Это выведет "My name is my name"
