import math
# from scipy.misc import derivative
import sympy

def print_result(p, n):
    print('O resultado p: %f' % p)
    print('Em n iterações: %d' % n)

def newton(f, aproximacao_inicial, precisao, iteracoes):
    x = sympy.symbols('x')
    funcao = sympy.utilities.lambdify(x, f)
    derivada = sympy.utilities.lambdify(x, sympy.diff(f, x))

    i = 1
    while i <= iteracoes:
        aproximacao_final = aproximacao_inicial - funcao(aproximacao_inicial) / derivada(aproximacao_inicial)
        if math.fabs(aproximacao_final - aproximacao_inicial) <= precisao:
            print_result(aproximacao_final, i)
            return aproximacao_final
        aproximacao_inicial = aproximacao_final

        i = i + 1

    print(f'O método falhou apos {iteracoes} iterações')
