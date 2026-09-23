def format_record(rec: tuple[str, str, float]) -> str:
    """Format a student record as a human-readable string.

    Args:
        rec: tuple[str, str, float]

    Returns:
        Formated string from tuple.
        Type: str.

    Raises:
        ValueError: If fio contains fewer than 2 parts.
        TypeError: If rec is not a tuple of three elements.
    """
    fio, group, gpa = rec
    fio_parts = fio.strip().split()

    if len(fio_parts) < 2:
        raise ValueError("FIO must contain at least surname and name.")

    surname = fio_parts[0].capitalize()

    initials = "".join(part[0].upper() + "." for part in fio_parts[1:])

    group_clean = " ".join(group.strip().split())

    return f"{surname} {initials}, гр. {group_clean}, GPA {gpa:.2f}"


print(format_record( ("Иванов Иван Иванович", "BIVT-25", 4.6) ))
print(format_record( ("Петров Пётр", "IKBO-12", 5.0) ))
print(format_record( ("Петров Пётр Петрович", "IKBO-12", 5.0) ))
print(format_record( ("  сидорова  анна   сергеевна ", "ABB-01", 3.999) ))