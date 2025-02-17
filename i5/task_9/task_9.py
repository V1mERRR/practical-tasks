Number = int | float | complex


# Write the function that doubles each element
# from list `l`.
#
# NOTE: that function modifies list `l` inplace;
# it should return nothing.
def double(l: list[Number]):
    for i in range(len(l)):  # Проходим по индексу каждого элемента
        l[i] *= 2  # Удваиваем элемент на месте


# Do not change the below's code
if __name__ == "__main__":
    l = [3, 4, 1, 2]
    double(l)
    print("After:", l)  # Выводим список после изменения
    assert l == [6, 8, 2, 4]  # Убедитесь, что проверяется правильный список

    l = [2, 2]
    double(l)
    assert l == [4, 4]

    l = [0.2, 0.4]
    double(l)
    assert l == [0.4, 0.8]
