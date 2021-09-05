import math

def print_result(p, n):
    print('O resultado p: %f' % p)
    print('Em n iterações: %d' % n)


def posicao_falsa(funcao, limite_inicial, limite_final, precisao, iteracoes):
    if funcao(limite_inicial)*funcao(limite_final) > 0:
        return 'A função não possui raiz no intervalo'
    if limite_inicial >= limite_final:
        return 'Este procedimento não aceita a>=b'
    if precisao <=0:
        return 'Tolerância é necessário ser maior que 0'
    if iteracoes <=0:
        return 'O número de iterações precisa ser maior que 0'
    if funcao(limite_inicial) == 0:
        print_result(limite_inicial, 0)
        return (limite_inicial, 0)
    if funcao(limite_final) == 0:
        print_result(limite_final, 0)
        return (limite_final, 0)
    
    i = 1
    f_a = funcao(limite_inicial)

    while i <= iteracoes:
        point = (((limite_inicial*funcao(limite_final))-(limite_final*funcao(limite_inicial))) / (funcao(limite_inicial) - funcao(limite_final)) )
        f_p = funcao(point)
        if f_p == 0 or (limite_final - limite_inicial) < precisao:
            print_result(point, i)
            return point
        if (f_a > 0) == (f_p > 0) or (f_a < 0) == (f_p < 0):
            limite_inicial = point
        else:
            limite_final = point
        i = i + 1
    return f'O método falhou apos {iteracoes} iterações'

