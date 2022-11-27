# Author: Dr. Baillif
#
# Petites fonctions pour manipuler des polynômes (avec coefficients en float).
# Attention: le Polynôme 3x^2 + 2x + 1 est codé comme [1,2,3]

def remove_zeros(p):
    m = len(p)
    n = 1
    while n <= m and p[-n] == 0:
        n += 1
    return p[:m-n+1]


def pol_string(p):
    s = ''
    for l, k in enumerate(p):
        if k != 0:
            if k < 0:
                s += ' '
            elif l > 0 and k > 0:
                s += ' + '
            if l == 0:
                s += str(k)
            else:
                if k != 1:
                    s += str(k)+'*'
                if l == 1:
                    s += 'x '
                if l > 1:
                    s += 'x^' + str(l)
    return s


def addition(a, b):
    m = max(len(a), len(b))
    s0 = [0 for k in range(m)]
    for k in range(m):
        if (k < len(a)):
            s0[k] += a[k]
        if (k < len(b)):
            s0[k] += b[k]
    return remove_zeros(s0)


def multiplication(a, b):
    prod = [0]*(len(a) + len(b) - 1)
    for k in range(len(a)):
        for l in range(len(b)):
            prod[k+l] += a[k]*b[l]
    return prod


def soustraction(a, b):
    return addition(a, multiplication(b, [-1]))
