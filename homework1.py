#!/usr/bin/env python3

from math import *

Lambda = 1.0/100.0
Mu = 1.0/2.0
a = 100
n = 5
P_reject_limit = 0.01


def get_mu_i(i):
    """
    :param i
    :returns Mu(i)
    """
    return Mu * i


def get_p_coeff(i):
    """
    :param i:
    """
    return pow(a, i) / factorial(i)


def get_p_0():
    temp = 0
    for i in range(0, n+1):
        temp += get_p_coeff(i)
    return 1 / temp


def get_p_i(i):
    """
    :param i:
    :returns P(i)
    """
    return get_p_coeff(i) * get_p_0()


def get_p_reject():
    return get_p_i(n)


def get_n_avg():
    N_avg = 0
    for i in range(0, n+1):
        N_avg += i * get_p_i(i)
    return N_avg


def get_n_avg_rel():
    return get_n_avg() / n

###########################################
while get_p_reject() > P_reject_limit:
    n += 1
print('P_rej={0:.3f} for reject limit {1:.2f} with n={2:d}'.format(get_p_reject(), P_reject_limit, n))
print('N_avg={0:.2f}'.format(get_n_avg()))
print('N_avg_rel={0:.1f} %'.format(get_n_avg_rel() * 100))


