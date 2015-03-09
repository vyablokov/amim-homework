#!/usr/bin/env python3

import matplotlib.pyplot as plt

def breaking_calculation(probablity):
    breaking = 0
    for i in range(len(probablity)):
        breaking += i * probablity[i]
    return breaking

def zero_probability_calculation(coefficiency_probabilty):
    zero_p = 0
    sum_coef = 0
    for i in range(len(coefficiency_probabilty)):
        sum_coef += coefficiency_probabilty[i]
    zero_p = 1/sum_coef
    return zero_p

def probability_calculation(zero_probability, coefficiency_probabilty):
    cur_p = []
    for i in range(len(coefficiency_probabilty)):
        cur_p.append(zero_probability * coefficiency_probabilty[i])
    return cur_p

def solution(num_of_workers, a, n):
    coef = [1]
    for i in range(1, num_of_workers):
        coef.append(coef[i-1]*(n-(i-1))*a/i)
    for i in range(num_of_workers, n+1):
        coef.append(coef[i-1]*(n-(i-1))*a/num_of_workers)
    zero_p = zero_probability_calculation(coef)
    p = probability_calculation(zero_p, coef)
    breaking = breaking_calculation(p)

    return breaking

"""
@param percentage - кол-во нерабочих станков в %
"""
def main(percentage, a, n):

    breaking_history = []
    succeed = False
    for i in range(1, n):
        breaking = solution(i, a, n)
        breaking_history.append(breaking)
        if breaking/n < percentage:
            succeed = True
            break
    if succeed:
        print("Требуется наладчиков:", i)
    else:
        print("Слишком много станков")

    plt.plot(range(1, 1+len(breaking_history)),
             breaking_history, label="N_avg")
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3)
    plt.show()


l = 1.0 / 67.0
m = 1.0 / 6.0
a = l/m
n = 13

main(0.10, a, n)