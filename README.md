# MAT221-1OL-MP
Machine Problem

## Introduction

This command-line tool solves a mathematical problem using numerical methods. The methods included are:

* Forward Finite Divided Difference
* Gauss Jacobi
* Newton Interpolation - Divided Difference
* Richardson Extrapolation 
* Secant Method
* Simpson's 1/3 Rule

## Getting Started

This tool requires [Python 3](https://www.python.org/downloads/) to run (>=py-3.9). Once you have Python 3 running,
run:

    ~$ python nmopde -h

This will show the __helper__ which describes how to use the tool.

> [!TIP]
> Export the directory to the PATH in order to run the tool without "python"
> For example, if you have the tool under /home/user, on a linux machine:

    ~$ export PATH=/home/user/MAT221-10L-MP:$PATH
    ~$ nmopde -h

## Methods

This tool provides different numerical methods.

### Forward Finite Divided Difference

To use Forward Finite Divided Difference:

    ~$ nmopde fdd -h
    ~$ nmopde fdd -x 0.5 -s 0.25 -f "-0.1*(x^4) - 0.15*(x^3) - 0.5*(x^2) - 0.25*x + 1.2"

This will give an output for the following:
1. Truncated
2. More Accurate

### Gauss Jacobi

To use Gauss Jacobi:

    ~$ nmopde gauss_jacobi -h
    ~$ nmopde gauss_jacobi -x 0 -y 0 -z 0 -fx "(3+y+z)/4" -fy "(9+2*x-z)/6" -fz "(-6+x-y)/7" -e 0.00001

### Newton Interpolation - Divided Difference

To use Newton Interpolation:

    ~$ nmopde newton_interpolation -h
    ~$ nmopde newton_interpolation -x "5,10,15,20,25,30,35" -y "5.02375,41.095,25.87625,34.78,40.46875,10.355,4.10125" -p 32.5

### Richardson Extrapolation

To use Richardson Extrapolation to improve the to FDD truncated solution:

    ~$ nmopde richardson_extrapolation -h
    ~$ nmopde richardson_extrapolation -x 0.5 -s "0.5,0.25" -f "-0.1*(x^4) - 0.15*(x^3) - 0.5*(x^2) - 0.25*x + 1.2"

### Secant Method

To use Secant Method:

    ~$ nmopde secant -h
    ~$ nmopde secant -f "(1 - x**2)**2 + 0.05963364 * x**2 - 0.25" -l 0 -u 1 -e 0.00001

### Simpson's 1/3 Rule

To Use Simpson's 1/3 Rule:

    ~$ nmopde simpson13 -h
    ~$ nmopde simpson13 -f '(1/(sqrt(2*pi)))*e((-0.5)*x**2)' -l -2 -u 1.6 -s 4

## Development

### Method

To add more numerical methods, create the python file under ``methods/`` named as the alias of the method
- for example, ``gauss_jacobi.py`` for Gauss Jacobi and the class name is ``Gaussjacobi``. 

The class must have the following methods:

1. ``subparser`` - defines the positional argument and its options.
2. ``evaluate`` - acts as the entrypoint of the class. This method will call other private methods to run the logic.

### Errors

Errors are defined under ``utils/errors.py``. Add custom errors and import them as necessary.

### Validation

Validation are defined under ``utils/validation.py``. Add custom validations and import them as necessary.

### Operations

Operation are defined under ``utils/operation.py``. Add custom operations and import them as necessary.

### Output

Method output is defined under ``utils/output.py``. Add custom outputs and import them as necessary.