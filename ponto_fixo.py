import math


def print_result(p, n):
    print('O resultado p: %f' % p)
    print('Em n iterações: %d' % n)


def ponto_fixo(func, p_0, precisao):
    i = 1

    while i <= 1000:
        point = func(p_0)

        if math.fabs(point - p_0) <= precisao:
            print_result(point, i)
            return

        i = i + 1

        p_0 = point

    print('O método falhou após {i} iterações')
