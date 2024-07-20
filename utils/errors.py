import sys


def _exit_error():
    sys.exit(1)


def function_invalid(f):
    print(f"[ERROR]: Invalid input function: '{f}'")
    _exit_error()


def function_compute(f):
    print(f"[ERROR]: Function compute error for: {f}")
    _exit_error()

def segments_invalid(h):
    print(f"[ERROR]: Invalid segments: {h}")
    _exit_error()