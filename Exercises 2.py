# Exercises 2.
#
# 1:
# Electricity buying prize per kWh: f(x) = 1 - 0.01*x
# Electricity selling prize per kWh: g(x) = 2 - 0.01*x
# Electricity buying limits: 0 <= x <= 50
# Maximize F(x) = g(x)*x - f(x)*x
#
# Formulate an optimization problem.
#
# Solution:
#   min    F(x) = (1 - 0.01*x)*x - (2 - 0.01*x**2)*x
#   s.t    -x  <= 0,
#          x   <= 50.
#

from math import sqrt


def func(x):
    return (1-x)**2 + x


# 2:
def bisection(f, a, b, l, eps=0.001):
    """Uses bisection search to find l-approximation of the optimal solution to the problem
        min  f(x)
        s.t. a <= x <= b"""
    while eps >= l:     # This makes sure that the algorithm doesn't get stuck in an endless loop.
        eps = eps * 0.1
    x, y = float(a), float(b)
    while y - x > l:
        c = (x+y)/2
        if f(c-eps) < f(c+eps):
            y = c + eps
        else:
            x = c - eps
    return (x+y)/2


print("Optimal solution by bisection search: " + str(bisection(func, 0, 2, 0.001)))


# 3:
def golden(f, a, b, l):
    """Uses golden section search to find l-approximation of the optimal solution to the problem
        min  f(x)
        s.t. a <= x <= b"""
    x, y, g = float(a), float(b), (sqrt(5)-1)/2
    while y - x > l:
        s = y - g*(y - x)
        t = x + g*(y - x)
        if f(s) < f(t):
            y = t
        else:
            x = s
    return (x+y)/2


print("Optimal solution by golden section search: " + str(golden(func, 0, 2, 0.001)))


# 4:
