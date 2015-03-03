#!/usr/bin/env python3

from math import *

Lambda = 1.0/5.0
Mu = 1.0/2.0
a = 4
n = 5
P_reject_limit = 0.1

def getMui(i):
    """
    :param i
    :returns Mu(i)
    """
    return  Mu * i

def getPCoeff(i):
    """
    :param i:
    """
    return pow(a, i) / factorial(i)

def getP0():
    temp = 0
    for i in range(0, n+1):
        temp += getPCoeff(i)
    return 1 / temp

def getPi(i):
    """
    :param i:
    :returns P(i)
    """
    return getPCoeff(i) * getP0()

def getPReject():
    return getPi(n)

def getNAvg():
    N_avg = 0
    for i in range(0, n+1):
        N_avg += i * getPi(i)
    return N_avg

def getNAvgRel():
    return getNAvg() / n

###########################################
while getPReject() > P_reject_limit:
    n += 1
print('P_rej={0:.3f} for reject limit {1:.2f} with n={2:d}'.format(getPReject(), P_reject_limit, n))
print('N_avg={0:.2f}'.format(getNAvg()))
print('N_avg_rel={0:.1f} %'.format(getNAvgRel() * 100))


