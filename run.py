from math import cos, e, sin, log10
import bisection
from posicao_falsa import posicao_falsa

def ex_18(x):
    return e**(-x**2) - cos(x)


def ex_19(x):
    return x**3 - x - 1


def ex_20(x):
    return 4*sin(x) - e**x


def ex_21(x):
    return x*log10(x) - 1


def test_bisection():
    limite_inicial = 1
    limite_final = 2
    tol = 1e-4

    bisection.bisection(ex_18, limite_inicial, limite_final, tol)

    limite_inicial = 1
    limite_final = 2
    tol = 1e-6

    bisection.bisection(ex_19, limite_inicial, limite_final, tol)

    limite_inicial = 0
    limite_final = 1
    tol = 1e-5

    bisection.bisection(ex_20, limite_inicial, limite_final, tol)

    limite_inicial = 2
    limite_final = 3
    tol = 1e-7

    bisection.bisection(ex_21, limite_inicial, limite_final, tol)


# test_bisection()

def test_posicao_falsa():
    limite_inicial = 1
    limite_final = 2
    tol = 1e-4
    it = 1000

    posicao_falsa(ex_18, limite_inicial, limite_final, tol, it)

    limite_inicial = 1
    limite_final = 2
    tol = 1e-6

    posicao_falsa(ex_19, limite_inicial, limite_final, tol, it)

    limite_inicial = 0
    limite_final = 1
    tol = 1e-5

    posicao_falsa(ex_20, limite_inicial, limite_final, tol, it)

    limite_inicial = 2
    limite_final = 3
    tol = 1e-7

    posicao_falsa(ex_21, limite_inicial, limite_final, tol, it)


test_posicao_falsa()
