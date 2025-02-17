# Write a function that returns `max(len(s), n)`
# characters from the middle of the string.
#
# For example,
# 1. middle("abddcvbn", 4) -> "ddcv"
# 2. middle("abddcvbn", 3) -> "ddc"
#
# NOTE: use // division to define slice start index
def middle(s: str, n: int) -> str:
    length = max(len(s), n)
    start = (len(s) - length) // 2
    return s[start:start + length]


# Do not change the below's code
if __name__ == "__main__":
    assert middle("abddcvbn", 4) == "ddcv"
    assert middle("abddcvbn", 3) == "ddc"
    assert middle("dcd", 5) == "dcd"
    assert middle("", 10) == ""
