import math
from scipy.misc import derivative
from sympy import diff

def print_result(p, n):
    print('O resultado p: %f' % p)
    print('Em n iterações: %d' % n)

def newton(funcao, aproximacao_inicial, precisao, iteracoes):
    i = 1
    while i <= iteracoes:
        aproximacao_final = aproximacao_inicial - funcao(aproximacao_inicial) / derivative(funcao,aproximacao_inicial)
        if math.fabs(aproximacao_final - aproximacao_inicial) <= precisao:
            print_result(aproximacao_final, i)
            return aproximacao_final
        i = i + 1
        aproximacao_inicial = aproximacao_final
    return f'O método falhou apos {iteracoes} iterações'
 