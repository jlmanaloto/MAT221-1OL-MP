from utils.errors import function_invalid
from utils.validation import function_validation
from utils.operations import func, function_parser, rounder
from utils.output import out


class Simpson13:
    def __init__(self):
        pass

    def subparser(self, sp):
        subparser = sp.add_parser(
            "simpson13",
            help="Simpson's 1/3 Rule.",
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
            "-s",
            "--segments",
            action="store",
            help="Absolute error.",
            type=int,
        )

    def _simpson13(self, a, b, n, f, r, v):
        print("\n*** Simpson's 1/3 Rule ***\n")
        data = [
            ["x", "f(x)", "Simpson's 1/3 Rule", ""]
        ]

        h_ans = (b - a) / n
        h = rounder(h_ans, 5)

        values = []
        x = a

        for segment in range(n+1):
            x_n = func(f, x, r, v)
            if segment > 0 and segment < n:
                if segment % 2 == 0:
                    mult = 2
                else:
                    mult = 4
            else:
                mult = 1

            val = mult * x_n

            data.append([x, x_n, mult, val])

            values.append(val)
            x = rounder((x+h), 5)

        total = rounder(sum(values), 5)
        data.append(["","","Σf(xi)",total])
        out(data)


        I_ans = (h / 3) * total
        I = rounder(I_ans, 5)
        print(f"I = {I}")

    def evaluate(self, args):
        if not function_validation(args.function):
            function_invalid(args.function)

        f = function_parser(args.function)
        self._simpson13(args.lower_bound, args.upper_bound, args.segments, f, args.round, args.variable)