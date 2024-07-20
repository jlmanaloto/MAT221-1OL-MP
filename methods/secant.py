from utils.errors import function_compute, function_invalid
from utils.validation import function_validation
from utils.operations import func, function_parser, rounder
from utils.output import out


class Secant:
    def __init__(self):
        pass

    def subparser(self, sp):
        subparser = sp.add_parser(
            "secant",
            help="Secant method.",
        )
        subparser.add_argument(
            "-f",
            "--function",
            action="store",
            help="Function to use the method against.",
            type=str,

        )
        subparser.add_argument(
            "-l",
            "--lower-bound",
            action="store",
            help="Lower bound of the Secant Method.",
            type=float,

        )
        subparser.add_argument(
            "-u",
            "--upper-bound",
            action="store",
            help="Upper bound of the Secant Method.",
            type=float,

        )
        subparser.add_argument(
            "-e",
            "--error",
            action="store",
            help="Absolute error.",
            type=float,

        )

    def _secant(self, x0, x1, e, f, r, v):
        print('\n*** SECANT METHOD ***\n')
        data = [
            ["Iteration", "x0", "f(x0)", "x1", "f(x1)", "x2", "f(x2)"]
        ]
        step = 1
        condition = True
        while condition:
            fx0 = func(f, x0, r, v)
            fx1 = func(f, x1, r, v)
            if fx0 == fx1:
                function_compute(f)

            x2 = rounder((x0 - (x1-x0)*fx0/(fx1 - fx0)), r)
            fx2 = func(f, x2, r, v)
            data.append([step, x0, fx0, x1, fx1, x2, fx2])

            x0 = x1
            x1 = x2
            step = step + 1

            condition = abs(fx2) > e
        out(data)
        print(f"\nRoot: {x2}")

    def evaluate(self, args):
        if not function_validation(args.function):
            function_invalid(args.function)

        f = function_parser(args.function)
        self._secant(args.lower_bound, args.upper_bound, args.error, f, args.round, args.variable)