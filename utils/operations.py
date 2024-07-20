import decimal
from math import cos, sin, pi, sqrt, pow as power, exp as e


def function_parser(fraw: str):
    f = fraw.replace("^", "**")
    return f


def rounder(n: float, r: int):
    d = decimal.Decimal(str(n))
    return float(round(d, r))


def func(f: str, n, r, var, **kwargs):
    if kwargs:
        x = kwargs.get("x", 0)
        y = kwargs.get("y", 0)
        z = kwargs.get("z", 0)
    f = f.replace(var, "n")
    f = f.replace("e^", "e")
    f_ans = eval(f)
    ans = rounder(f_ans, r)
    return ans