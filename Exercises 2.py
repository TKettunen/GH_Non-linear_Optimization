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
# Use differentiation to find solutions to the problems in 1 and 2.
#
# Solution:
# 1.
# F(x) = (1 - 0.01*x)*x - (2 - 0.01*x**2)*x
#      = x - 0.01*x**2 - 2*x + 0.01*x**3
#      = -x - 0.01x**2 + 0.01*x**3
#
# Find the roots of the derivative function:
# F'(x) = -1 - 0.02*x + 0.03*x**2 = 0
# <=> x = (0.02 (+/-) sqrt(0.02**2 - 4*0.03*(-1)))/(2*0.03)
# <=> x = 6.12 OR x = -5.45
#
# interval between the roots of derivative and increasing after that.
# Thus the minimum solution is at the point x = 6.12. This solution is feasible so
# it is also the optimal solution. The value in that point is F(6.12) = -4.2.
#
# 2.
# f(x) = (1-x)**2 + x
# f'(x) = 2*(1-x)*(-1) + 1
#       = 2*x - 1
#
# Find the roots of the derivative function:
# f'(x) = 0  <=>  x = 0.5
#
# The minimal solution is x = 0.5. This is also feasible so it is the optimal solution.
# The value in this solution is f(0.5) = 0.75.
