from utils.errors import function_invalid
from utils.validation import function_validation
from utils.operations import func, function_parser, rounder


class Fdd:
    def __init__(self):
        pass

    def subparser(self, sp):
        subparser = sp.add_parser(
            "fdd",
            help="Forward Divided Difference.",
        )
        subparser.add_argument(
            "-f",
            "--function",
            action="store",
            help="Function to use the method against.",
            type=str,

        )
        subparser.add_argument(
            "-x",
            dest="pointx",
            action="store",
            help="Value of xi.",
            type=float,

        )
        subparser.add_argument(
            "-s",
            "--segments",
            action="store",
            help="Segments for the Forward Divided Difference.",
            type=float,

        )
        subparser.add_argument(
            "-r",
            "--round",
            action="store",
            default=5,
            help="Decimal places to round off.",
            type=int,
        )
        subparser.add_argument(
            "-v",
            "--variable",
            action="store",
            default="x",
            help="Specify the variable of the function. Defaults to 'x'.",
            type=str,
        )

    def _fdd_trunc(self, xi, h, f, r, v):
        xi1 = xi + h
        fpx = rounder(
            (
                (
                    func(f, xi1, r, v) - func(f, xi, r, v)
                ) / h
            ),
            r,
        )
        print(f"xi = {xi} | xi+1 = {xi1}")
        print(f"f'(xi) = {fpx}")
        return fpx

    def _fdd_acc(self, xi, h, f, r, v):
        xi1 = xi+h
        xi2 = xi+(2*h)
        f1 = func(f, xi2, r, v)
        f2 = func(f, xi1, r, v)
        f3 = func(f, xi, r, v)
        print(f"xi = {xi} | xi+1 = {xi1} | xi+2 = {xi2}")
        print(f"f(xi) = {f3} | f(xi+1) = {f2} | f(xi+2) = {f1}")
        fpx = rounder(
            (
                (
                    (
                        -func(f, xi2, r, v)
                    ) + (
                        4*func(f, xi1, r, v)
                    ) - (
                        3*func(f, xi, r, v)
                    )
                ) / (2*h)
            ),
            r,
        )
        print(f"f'(xi) = {fpx}")
        return fpx

    def evaluate(self, args):
        if not function_validation(args.function):
            function_invalid(args.function)

        f = function_parser(args.function)
        print("\n*** Forward Divided Difference ***")
        print("\n--- Truncated ---\n")
        _ = self._fdd_trunc(args.pointx, args.segments, f, args.round, args.variable)
        print("\n--- More Accurate ---\n")
        _ = self._fdd_acc(args.pointx, args.segments, f, args.round, args.variable)
