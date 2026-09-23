def transpose(mat: list[list[float | int]]) -> list[list]:
    """Transpose a rectangular matrix (swap rows and columns).

    Args:
        mat: list [ list [float | int] ]

    Returns:
        New matrix where rows and columns are swapped.
        Type: list[list]

    Raises:
        ValueError: If matrix is not rectangular.
    """
    if not mat:
        return []

    rows = len(mat)
    cols = len(mat[0])

    for row in mat:
        if len(row) != cols:
            raise ValueError("Matrix is not rectangular.")

    result: list[list] = []
    for c in range(cols):
        new_row: list = []
        for r in range(rows):
            new_row.append(mat[r][c])
        result.append(new_row)

    return result


def row_sums(mat: list[list[float | int]]) -> list[float]:
    """Return a list with the sum of each row of a rectangular matrix.

    Args:
        mat: list[ list [float | int] ]

    Returns:
        List of row sums.
        Type: list[float]

    Raises:
        ValueError: If matrix is not rectangular.
    """
    if not mat:
        return []

    cols = len(mat[0])
    for row in mat:
        if len(row) != cols:
            raise ValueError("Matrix is not rectangular.")

    result: list[float] = []
    for row in mat:
        total = 0
        for value in row:
            total += value
        result.append(total)

    return result


def col_sums(mat: list[list[float | int]]) -> list[float]:
    """Return a list with the sum of each column of a rectangular matrix.

    Args:
        list[ list [float | int] ]

    Returns:
        List of column sums.
        Type: list [float]

    Raises:
        ValueError: If matrix is not rectangular.
    """
    if not mat:
        return []

    rows = len(mat)
    cols = len(mat[0])

    for row in mat:
        if len(row) != cols:
            raise ValueError("Matrix is not rectangular.")

    result: list[float] = [0] * cols
    for r in range(rows):
        for c in range(cols):
            result[c] += mat[r][c]

    return result
