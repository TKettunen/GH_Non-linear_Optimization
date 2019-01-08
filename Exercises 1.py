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
    if grade < 0:
        return 0
    for i in range(0, maximum):
        if grade == give_grade(i, maximum):
            return i
    return ceil(0.9 * maximum)
