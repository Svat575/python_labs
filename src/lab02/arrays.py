def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    """Return a tuple (minimum, maximum) from a list of numbers.

    Args:
        nums: list [float or int]

    Returns:
        Type: tuple [float | int, float | int]

    Raises:
        ValueError: List is empty.
    """
    if not nums:
        raise ValueError("List is empty.")

    minimum = nums[0]
    maximum = nums[0]

    for value in nums[1:]:
        if value < minimum:
            minimum = value
        if value > maximum:
            maximum = value

    return minimum, maximum


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    """Return a list of unique values ​​sorted in ascending order.

    Args:
        nums: list [float | int]

    Returns:
        A new list containing only unique values, sorted in ascending order.
        Type: list [float | int]
    """

    unique: list[float | int] = []
    for value in nums:
        if value not in unique:
            unique.append(value)

    n = len(unique)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if unique[j] > unique[j + 1]:
                unique[j], unique[j + 1] = unique[j + 1], unique[j]

    return unique


def flatten(mat: list[list | tuple]) -> list:
    """Flatten a list of lists/tuples into a single list (row-major).

    Args:
       mat: list [list | tuple]

    Returns:
        Flatten list.
        Type: list

    Raises:
        TypeError: Unexpected 1 or more elements that aren't list or tuple.
    """
    result: list = []

    for row in mat:
        if not isinstance(row, (list, tuple)):
            raise TypeError("There are 1 or more elements that aren't list or tuple.")
        for item in row:
            result.append(item)

    return result

