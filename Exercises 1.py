from math import ceil


def give_grade(n, maximum=20):
    """Returns the grade you get by completing n points out of maximum."""
    x = float(n)/maximum
    if x < 0.5:
        return 0
    if x >= 1:
        return 5
    return int(x * 10 - 4)


def min_points(grade, maximum=20):
    """Returns the minimum number of points you need for the given grade."""
    if grade <= 0:
        return 0
    if grade >= 5:
        return ceil(0.9 * maximum)
    x = float(grade + 4) / 10
    return ceil(x * maximum)
