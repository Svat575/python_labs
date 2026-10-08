def format_record(rec: tuple[str, str, float]) -> str:
    """Format a student record as a human-readable string.

    Args:
        rec: tuple[str, str, float]

    Returns:
        Formated string from tuple.
        Type: str.

    Raises:
        ValueError: fio is empty.
        ValueError: groups is empty.
        TypeError: GPA isnt float.
    """
    fio, group, gpa = rec

    fio = " ".join(fio.split())

    if not fio:
        raise ValueError("Incorrect fio.")
    if not group:
        raise ValueError("Incorrect group.")
    if not isinstance(gpa, float):
        raise TypeError("Incorrect type for GPA.")

    name_parts = fio.split()
    surname = name_parts[0].capitalize()

    if len(name_parts) == 3:
        initials = f"{name_parts[1][0].upper()}. {name_parts[2][0].upper()}."
    else:
        initials = f"{name_parts[1][0].upper()}."

    return f"{surname} {initials}, гр. {group}, GPA {gpa:.2f}"
