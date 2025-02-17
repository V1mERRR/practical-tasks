if __name__ == "__main__":
    l = [1, 2, 0, 3]

    s = 0
    for i, v in enumerate(l):
        try:
            # Пытаемся выполнить деление
            s = i / v
        except ZeroDivisionError:
            # Если деление на ноль, просто продолжаем цикл
            continue
