
from utils.operations import func, rounder
from utils.output import out


def data_finalizer(data, length):
    for ld in data:
        if len(ld) != length:
            rlen = length - len(ld)
            for i in range(rlen):
                ld.append("")


def construct_output(data, val):
    for i in range(len(val)):
        data[i+1].append(str(val[i]))


class Newtoninterpolation:
    def __init__(self):
        pass

    def subparser(self, sp):
        subparser = sp.add_parser(
            "newton_interpolation",
            help="Newton's Interpolation.",
        )
        subparser.add_argument(
            "-x",
            dest="datax",
            action="store",
            help="Data point x.",
            type=str,
        )
        subparser.add_argument(
            "-y",
            dest="datay",
            action="store",
            help="Data point y or f(x).",
            type=str,
        )
        subparser.add_argument(
            "-p",
            "--predict",
            action="store",
            help="Predict this value of data point x.",
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

    def _bval(self, data):
        bval = f"{data[1][1]}"
        p = 1
        mult = ""
        for i in range(2, len(data)):
            val = data[1][i]
            if float(val) >= 0:
                op = "+"
            else:
                op = ""
            mult = mult + f"*(x-{data[p][0]})"
            if mult.startswith("*"):
                mult = mult[1:]
            bval = bval + f"{op}{val}*({mult})"
            p+=1
        return bval

    def _nifdd(self, x, fx, n, r, v):
        print("\n*** Newton's Interpolation ***\n")
        data_fx = fx.copy()
        data_x_len = len(x)
        data = [
            ["x", "f(x)"] +
            [f"f{i+1}(x)" for i in range(data_x_len-1)]
        ]
        data_space = [
            [] for i in range(data_x_len)
        ]
        data = data + data_space

        construct_output(data, x)
        construct_output(data, fx)
        for i in range(data_x_len-1):
            data_fpx = []
            data_fx_len = len(data_fx)
            for j in range(data_fx_len-1):
                idx = abs(data_x_len - data_fx_len)
                fpx = rounder(
                    (
                        (data_fx[j+1] - data_fx[j]) / (x[j+idx+1] - x[j+idx-i])
                    ),
                    r,
                )
                data_fpx.append(fpx)
            data_fx = data_fpx.copy()
            construct_output(data, data_fx)
        data_finalizer(data, data_x_len+1)
        out(data)
        fp = func(self._bval(data), n, r, v)
        print(f"\nPredicted value f(x) = {fp}")

    def evaluate(self, args):
        data_x_str = str(args.datax).split(",")
        data_y_str = str(args.datay).split(",")
        data_x = [ float(i) for i in data_x_str ]
        data_y = [ float(i) for i in data_y_str ]
        self._nifdd(data_x, data_y, args.predict, args.round, args.variable)
