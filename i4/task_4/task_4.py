def find_max(l: list[int]) -> int | None:
    if not l:
        return None
    max_value = l[0]
    for num in l:
        if num > max_value:
            max_value = num
    return max_value


# Do not change the below's code
if __name__ == "__main__":
    assert find_max([3, 1, 4, 3]) == 4
    assert find_max([3, 1, 4, 3, 8, 7]) == 8
    assert find_max([1]) == 1
    assert find_max([]) == None
