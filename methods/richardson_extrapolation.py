from methods.fdd import Fdd
from utils.errors import function_invalid, segments_invalid
from utils.validation import function_validation
from utils.operations import function_parser, rounder


class Richardsonextrapolation:
    def __init__(self):
        pass

    def subparser(self, sp):
        subparser = sp.add_parser(
            "richardson_extrapolation",
            help="Richardson Extrapolation to improve FDD.",
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
            help="Segments (h) to use. Specify a maximum of two segments delimited by a comma.",
            type=str,
        )

    def _richardson(self, xi, segments, f, r, v):
        fdd = Fdd()
        vals = []
        print(f"From FDD (truncated) values\n")
        for segment in segments:
            d = fdd._fdd_trunc(xi, segment, f, r, v)
            vals.append(d)
            print("\n")

        D = rounder(((4/3)*(vals[0]) - (1/3)*(vals[1])), r)
        print(f"D = {D}")

    def evaluate(self, args):
        if not function_validation(args.function):
            function_invalid(args.function)

        f = function_parser(args.function)
        segments = str(args.segments).split(",")
        if len(segments) != 2:
            segments_invalid(segments)
        h = [float(segment) for segment in segments]
        h.sort()
        print("\n*** Richardson Extrapolation ***")
        _ = self._richardson(args.pointx, h, f, args.round, args.variable)