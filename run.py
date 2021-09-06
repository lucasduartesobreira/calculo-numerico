import math
from bisection import bisection
from posicao_falsa import posicao_falsa
from ponto_fixo import ponto_fixo
from newton import newton
# from sympy import diff, symbols
from sympy import *
from secante import secante


def ex_18(x):
    return math.e**(-x**2) - math.cos(x)


def ex_19(x):
    return x**3 - x - 1


def ex_20(x):
    return 4*math.sin(x) - math.e**x


def ex_21(x):
    return x*math.log10(x) - 1


def test_bisection():
    limite_inicial = 1
    limite_final = 2
    tol = 1e-4

    bisection(ex_18, limite_inicial, limite_final, tol)

    limite_inicial = 1
    limite_final = 2
    tol = 1e-6

    bisection(ex_19, limite_inicial, limite_final, tol)

    limite_inicial = 0
    limite_final = 1
    tol = 1e-5

    bisection(ex_20, limite_inicial, limite_final, tol)

    limite_inicial = 2
    limite_final = 3
    tol = 1e-7

    bisection(ex_21, limite_inicial, limite_final, tol)


print('---Teste do método da bisecção---')
test_bisection()


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


print('---Teste do método da posição falsa---')
test_posicao_falsa()


def mpf_ex_18(x):
    return math.cos(x) - math.e**(-x**2) + x


def mpf_ex_19(x):
    return (x+1)**(1/3)


def mpf_ex_20(x):
    return x-2*math.sin(x)+0.5*math.e**x


def mpf_ex_21(x):
    return x-1.3*(x*math.log10(x) - 1)


def test_ponto_fixo():
    p_0 = 1.5
    tol = 1e-4

    ponto_fixo(mpf_ex_18, p_0, tol)

    p_0 = 1
    tol = 1e-6

    ponto_fixo(mpf_ex_19, p_0, tol)

    p_0 = 0.5
    tol = 1e-5

    ponto_fixo(mpf_ex_20, p_0, tol)

    p_0 = 2.5
    tol = 1e-7

    ponto_fixo(mpf_ex_21, p_0, tol)


print('---Teste do método do ponto fixo---')
test_ponto_fixo()


def test_newton():
    x = symbols('x')

    p_0 = 1.5
    tol = 1e-4
    it = 1000
    expr_18 = exp(-x**2)-cos(x)

    newton(expr_18, p_0, tol, it)

    p_0 = 1
    tol = 1e-6
    expr_19 = x**3-x-1

    newton(expr_19, p_0, tol, it)

    p_0 = 0.5
    tol = 1e-5
    expr_20 = 4*sin(x) - exp(x)

    newton(expr_20, p_0, tol, it)

    p_0 = 2.5
    tol = 1e-7
    expr_21 = ( x*log(x,10) - 1 )

    newton(expr_21, p_0, tol, it)


print('---Teste do método do newton---')
test_newton()


def test_secante():
    it = 1000

    p_0 = 1
    p_1 = 2
    tol = 1e-4

    secante(ex_18, p_0, p_1, tol, it)

    p_0 = 0
    p_1 = 0.5
    tol = 1e-6

    secante(ex_19, p_0, p_1, tol, it)

    p_0 = 0
    p_1 = 1
    tol = 1e-5

    secante(ex_20, p_0, p_1, tol, it)

    p_0 = 2.3
    p_1 = 2.7
    tol = 1e-7

    secante(ex_21, p_0, p_1, tol, it)


print('---Teste do método da secante---')
test_secante()
