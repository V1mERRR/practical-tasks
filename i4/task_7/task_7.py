def count_digits(n: int) -> int:
    count = 0
    while n > 0:
        count += 1
        n //= 10  # Уменьшаем число, удаляя последнюю цифру
    return count if count > 0 else 1  # Если число равно 0, то считаем, что цифра 1


# Do not change the below's code
if __name__ == "__main__":
    assert count_digits(0) == 1
    assert count_digits(134) == 3
    assert count_digits(54) == 2
    assert count_digits(55678) == 5
