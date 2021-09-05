from math import cos, e
import bisection


def f(x):
    return e**(-x**2) - cos(x)


def run_bisection():
    limite_inicial = float(input('Limite inicial: '))
    limite_final = float(input('Limite final: '))
    tol = float(input('Tol: '))

    bisection.bisection(f, limite_inicial, limite_final, tol)


run_bisection()
