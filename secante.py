import math


def print_result(p, n):
    print('O resultado p: %f' % p)
    print('Em n iterações: %d' % n)


def secante(funcao, p_0, p_1, precisao, iteracoes):
    i = 2
    q_0 = funcao(p_0)
    q_1 = funcao(p_1)

    while i <= iteracoes:
        point = p_1 - q_1*(p_1 - p_0)/(q_1 - q_0)

        if math.fabs(point - p_1) <= precisao:
            print_result(point, i)
            return point

        p_0 = p_1
        q_0 = q_1
        p_1 = point
        q_1 = funcao(point)

        i = i + 1

    print(f'O método falhou apos {iteracoes} iterações')
