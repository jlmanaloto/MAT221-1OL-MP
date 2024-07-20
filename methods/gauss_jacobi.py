from utils.errors import function_invalid
from utils.validation import function_validation
from utils.operations import func, rounder
from utils.output import out


class Gaussjacobi:
    def __init__(self):
        pass

    def subparser(self, sp):
        subparser = sp.add_parser(
            "gauss_jacobi",
            help="Gauss-Jacobi method.",
        )
        subparser.add_argument(
            "-x",
            dest="x",
            action="store",
            help="Function to use the method against.",
            required=True,
            type=float,

        )
        subparser.add_argument(
            "-y",
            dest="y",
            action="store",
            help="Function to use the method against.",
            required=True,
            type=float,

        )
        subparser.add_argument(
            "-z",
            dest="z",
            action="store",
            help="Function to use the method against.",
            required=True,
            type=float,

        )
        subparser.add_argument(
            "-fx",
            dest="fx",
            action="store",
            help="Diagonally dominant equation for variable x.",
            required=True,
            type=str,

        )
        subparser.add_argument(
            "-fy",
            dest="fy",
            action="store",
            help="Diagonally dominant equation for variable y.",
            required=True,
            type=str,

        )
        subparser.add_argument(
            "-fz",
            dest="fz",
            action="store",
            help="Diagonally dominant equation for variable z.",
            required=True,
            type=str,

        )
        subparser.add_argument(
            "-e",
            "--error",
            action="store",
            help="Tolerable error.",
            required=True,
            type=float,

        )

    def _jacobi(self, x, y, z, fx, fy, fz, e, r, v):
        count = 0
        data = [
            ["n", "x", "y", "z"]
        ]
        while True:
            x_n = func(fx, 0, r, "g", x=x, y=y, z=z)
            y_n = func(fy, 0, r, "g", x=x, y=y, z=z)
            z_n = func(fz, 0, r, "g", x=x, y=y, z=z)
            e_x = rounder(abs(x-x_n), r)
            e_y = rounder(abs(y-y_n), r)
            e_z = rounder(abs(z-z_n), r)

            data.append(
                [
                    str(count),
                    str(x_n),
                    str(y_n),
                    str(z_n),
                ]
            )

            count+=1
            x = x_n
            y = y_n
            z = z_n

            if e_x <= e and e_y <= e and e_z <= e:
                break
        out(data)
        print(f"\nx = {x}\ty = {y}\tz = {z}")

    def evaluate(self, args):
        print(f"jacobi: {args}")
        for f in [args.fx, args.fy, args.fz]:
            if not function_validation(f):
                function_invalid(f)

        print("\n*** Gauss Jacobi ***")
        self._jacobi(
            args.x,
            args.y,
            args.z,
            args.fx,
            args.fy,
            args.fz,
            args.error,
            args.round,
            args.variable,
        )