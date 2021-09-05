import math
from math import cos, e


def f(x):
    return e**(-x**2) - cos(x)


def print_result(p, n):
    print('O resultado p: %f' % p)
    print('Em n iterações: %d' % n)


def bisection(func, limite_inicial, limite_final, precisao):
    if func(limite_inicial) * func(limite_final) > 0:
        return 'A função não possui raiz no intervalo'
    if limite_inicial >= limite_final:
        return 'Este procedimento não aceita a >= b'
    if precisao <= 0:
        return 'Tolerância é necessário ser maior que 0'
    if func(limite_inicial) == 0:
        print_result(limite_inicial, 0)
        return (limite_inicial, 0)
    if func(limite_final) == 0:
        print_result(limite_final, 0)
        return (limite_final, 0)

    i = 1
    f_a = func(limite_inicial)
    um_sobre_log_2 = 1/math.log10(2)
    n_0 = um_sobre_log_2*(math.log10((limite_final-limite_inicial)/precisao))
    n_0 = math.ceil(n_0)

    while i <= n_0:
        point = (limite_final+limite_inicial)/2
        f_p = func(point)
        if f_p == 0 or (limite_final-limite_inicial)/2 < precisao:
            print_result(point, i)
            return point

        if (f_a > 0) == (f_p > 0) or (f_a < 0) == (f_p < 0):
            limite_inicial = point
        else:
            limite_final = point

        i = i + 1

    return f'O método falhou apos {n_0} iterações'


# print(bisection(f, 1.0, 2.0, 1e-4))
