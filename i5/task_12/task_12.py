from typing import Any

# Write a function that extends list `l1` with elements
# from list `l2`.
def proxy_extend(l1: list[Any], l2: list[Any]):
    l1.extend(l2)  # Расширяем l1 элементами из l2

# Do not change the below's code
if __name__ == "__main__":
    l1, l2 = [1, 2, 3], [4, 5, 6]
    proxy_extend(l1, l2)
    assert l1 == [1, 2, 3, 4, 5, 6]
    assert l2 == [4, 5, 6]
