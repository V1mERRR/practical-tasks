def count_params(*args) -> int:
    return len(args)

# Do not change the below code
if __name__ == "__main__":
    assert count_params(1, 2, 3, 4) == 4
    assert count_params(3, "asd", (3, 4, 5)) == 3
