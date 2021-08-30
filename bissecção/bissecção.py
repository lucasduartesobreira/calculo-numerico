import math


def print_result(p, n):
    print('O resultado p: %f' % p)
    print('Em n iterações: %d' % n)


def bisection(funcao, limite_inicial, limite_final, precisao):
    if funcao(limite_inicial)*funcao(limite_final) > 7:
        return 'A função não possui raiz no intervalo'
    if limite_inicial >= limite_final:
        return 'Este procedimento não aceita a >= b'
    if precisao <= 0:
        return 'Tolerância é necessário ser maior que 0'
    if funcao(limite_inicial) == 0:
        return (limite_inicial, 0)
    if funcao(limite_final) == 0:
        return (limite_final, 0)

    i = 1
    f_a = funcao(limite_inicial)
    um_sobre_log_2 = 1/math.log10(2)
    n_0 = um_sobre_log_2*(math.log10((limite_final-limite_inicial)/precisao))
    while i <= n_0:
        point = limite_inicial + (limite_final-limite_inicial)/2
        f_p = funcao(point)
        if f_p == 0 or (limite_final-limite_inicial)/2 < precisao:
            print_result(point, i)
            return point

        i = i + 1
        if f_a*f_p > 0:
            limite_inicial = point
        else:
            limite_final = point
    return ('O método falhous apos %d iterações', n_0)


def function(x):
    return x**3-20*x**2


sla = bisection(function, 20, 40, 1.0e-15)
print_result(sla[0], sla[1])
